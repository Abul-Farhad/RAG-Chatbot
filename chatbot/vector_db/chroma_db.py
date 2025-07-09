from langchain_ollama.embeddings import OllamaEmbeddings
from langchain_chroma import Chroma
embedding_model = OllamaEmbeddings(model='mxbai-embed-large')
memory_vector_store = Chroma()
product_vector_store = Chroma()