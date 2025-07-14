from langchain_groq import ChatGroq
from dotenv import load_dotenv
from .baseLLM import BaseLLM
import os
load_dotenv()

class LLama3(BaseLLM):
    def __init__(self):
        self.llm = ChatGroq(model='llama-3.3-70b-versatile', api_key=os.getenv('GROQ_API_KEY'))
        super().__init__(model=self.llm)

class DeepseekR1(BaseLLM):
    def __init__(self):
        self.llm = ChatGroq(model='deepseek-r1-distill-llama-70b', api_key=os.getenv('GROQ_API_KEY'))
        super().__init__(model=self.llm)

class Gemma2(BaseLLM):
    def __init__(self):
        self.llm = ChatGroq(model='gemma2-9b-it', api_key=os.getenv('GROQ_API_KEY'))
        super().__init__(model=self.llm)

class Qwen(BaseLLM):
    def __init__(self):
        self.llm = ChatGroq(model='qwen-qwq-32b', api_key=os.getenv('GROQ_API_KEY'))
        super().__init__(model=self.llm)

class MistralSaba24b(BaseLLM):
    def __init__(self):
        self.llm = ChatGroq(model='mistral-saba-24b', api_key=os.getenv('GROQ_API_KEY'))
        super().__init__(model=self.llm)