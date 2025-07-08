from langchain_ollama.embeddings import OllamaEmbeddings
from langchain_chroma import Chroma
embedding_model = OllamaEmbeddings(model='mxbai-embed-large')
vector_store = Chroma(
    persist_directory='memory_vector_db',
    embedding_function=embedding_model,
    collection_name='chat_memory',
)