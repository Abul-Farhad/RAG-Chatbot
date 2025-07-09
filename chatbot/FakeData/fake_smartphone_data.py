import os
import json
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from langchain_chroma import Chroma
from chatbot.vector_db.chroma_db import embedding_model

_retriever_cache = None

def create_smartphone_documents(json_data):
    documents = []
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=400,
        chunk_overlap=50,
        length_function=len,
        is_separator_regex=False
    )

    for item in json_data:
        # Create comprehensive text content
        reviews = '. '.join(f"{user} said: {text}" for user, text in item['reviews'].items())
        text_content = f"""
        Brand: {item['Brand']}
        Model: {item['Model']}
        Price: {item['Price']}
        Quantity: {item['Quantity']}
        Reviews: {reviews}
        """
        # Create metadata
        metadata = {
            "brand": item["Brand"],
            "model": item["Model"],
            "price": int(item["Price"]),  # Store as numeric
            "quantity": item["Quantity"],
        }

        # Split text while preserving context
        texts = splitter.split_text(text_content)
        for text in texts:
            documents.append(Document(
                page_content=text,
                metadata=metadata
            ))

    return documents

def load_or_create_db():
    try:
        # This is the directory where this script is located
        base_dir = os.path.dirname(__file__)

        # ✅ Full path to the JSON file and vector DB directory
        json_path = os.path.join(base_dir, "fake_smartphone_data.json")
        persist_dir = os.path.join(base_dir, "smartphone_vector_db")

        print(f"📄 Looking for JSON at: {json_path}")
        print(f"💾 Using vector DB directory: {persist_dir}")

        if os.path.exists(persist_dir) and os.listdir(persist_dir):
            print("✅ Loading existing vector DB from disk.")
            return Chroma(persist_directory=persist_dir, embedding_function=embedding_model)
        else:
            print("📂 No existing DB found. Creating new vector DB.")
            if not os.path.exists(json_path):
                raise FileNotFoundError(f"🛑 JSON file not found at {json_path}")
            with open(json_path, "r", encoding="utf-8") as f:
                json_data = json.load(f)
            documents = create_smartphone_documents(json_data)
            return Chroma.from_documents(
                documents=documents,
                embedding=embedding_model,
                persist_directory=persist_dir
            )
    except Exception as e:
        print(f"❌ Error in load_or_create_db(): {e}")
        raise


# Initialize vector DB
def print_results(results):
    for result in results:
        print(result.page_content)


# fakesmartphonedata.py
def get_smartphone_retriever():
    global _retriever_cache
    if _retriever_cache is None:
        print("⚙️ Loading DB once...")
        _retriever_cache = load_or_create_db().as_retriever()
    return _retriever_cache

# if __name__ == "__main__":
#
#
#     smartphone_data_retriever = load_or_create_db().as_retriever()
#     query = "Samsung smartphones with price greater than 100000"
#     filter = {
#         "metadata":{
#             "price": {"$gte": 100000}
#         }
#
#     }
#
#     results = smartphone_vector_db.similarity_search(
#         query=query,
#         k=1,
#         filter=filter
#     )
#     results = smartphone_data_retriever.invoke(query, k=1)
#     for result in results:
#         print(result.metadata)
#
#     filter = {
#         "brand": "Apple",
#     }
#     query = "Iphone SE"
#     results = smartphone_vector_db.similarity_search(query=query, filter=filter)
#     for result in results:
#         print(result.metadata)
#     query = "Iphone SE"
#     results = smartphone_data_retriever.invoke(query, k=5)
#     print_results(results)


