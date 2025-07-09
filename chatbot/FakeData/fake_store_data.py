import os
import json
import requests
from langchain_text_splitters import RecursiveJsonSplitter
from oauthlib.uri_validate import query

from chatbot.vector_db.chroma_db import embedding_model
from langchain_chroma import Chroma

# Constants
persist_dir = "product_vector_db"
url = "https://dummyjson.com/products"

# Check if the persist directory exists
if os.path.exists(persist_dir) and os.listdir(persist_dir):
    # Load existing Chroma vector DB
    product_vector_db = Chroma(persist_directory=persist_dir, embedding_function=embedding_model)
    print("Loaded existing vector DB from disk.")
else:
    # Fetch and split data
    # Use individual products as texts
    products = requests.get(url).json()["products"]
    texts = [product for product in products]  # serialize each product

    # Now split them
    # print(texts)
    product_vector_db = Chroma()
    json_splitter = RecursiveJsonSplitter(max_chunk_size=300)
    docs = json_splitter.create_documents(texts=texts)

    # Create new vector DB and persist
    product_vector_db = Chroma.from_documents(
        documents=docs,
        embedding=embedding_model,
        persist_directory=persist_dir
    )
    print("Created and persisted new vector DB.")


# retriever = product_vector_db.as_retriever()
# query = "Mobile Accessories"
# results = retriever.invoke(query, k=3)
# for result in results:
#     print(f"Product: {result.page_content}, Metadata: {result.metadata}")
query = "Mobile Accessories"
results = product_vector_db.similarity_search(query)
print(results[0].page_content)