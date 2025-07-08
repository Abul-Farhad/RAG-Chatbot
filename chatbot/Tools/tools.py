from chatbot.vector_db.chat_memory_manager import ChatMemoryManager
from chatbot.vector_db.chroma_db import vector_store
from langchain.tools import tool

# @tool
# def retrieve_memory(query: str, session_id: str) -> str:
#     """
#     Retrieve relevant past messages from the vector store.
#
#     Args:
#         query (str): The query to search for in the memory.
#         session_id (str): The session ID to filter messages.
#         k (int): The number of results to return.
#
#     Returns:
#         list: A list of relevant messages.
#     """
#
#     print("--- Retrieving Memory ---")
#     chat_manager = ChatMemoryManager(vector_store=vector_store, session_id=session_id)
#     results = chat_manager.search_memory(query, k=3)
#     result = "\n".join([doc.page_content for doc in results])
#     print("Formatted results: ", result)
#     return result

tools = []