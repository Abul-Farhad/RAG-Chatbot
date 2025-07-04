from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
load_dotenv()


class GroqLLM:
    def __init__(self):
        self.llm = ChatGroq(model='gemma2-9b-it', api_key=os.getenv('GROQ_API_KEY'))

    def get_llm(self):
        return self.llm