import datetime

from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.documents import Document

class ChatMemoryManager:
    def __init__(self, vector_store, session_id: str):
        self.vector_store = vector_store
        self.session_id = session_id


    def search_memory(self, query, k=3):
        """Search relevant past messages"""
        results = self.vector_store.similarity_search(query, k=k)
        return results

    def add_message(self, message):
        """Store a message in the vector database with session context"""
        if isinstance(message, HumanMessage):
            metadata = {
                "type": "human",
                "timestamp": datetime.datetime.now().isoformat(),
                "session_id": self.session_id,
                "source": "chat"
            }
        elif isinstance(message, AIMessage):
            metadata = {
                "type": "ai",
                "timestamp": datetime.datetime.now().isoformat(),
                "session_id": self.session_id,
                "source": "chat"
            }
        else:
            return

        doc = Document(
            page_content=message.content,
            metadata=metadata
        )
        self.vector_store.add_documents([doc])