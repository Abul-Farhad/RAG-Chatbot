from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from .baseLLM import BaseLLM
import os
load_dotenv()


class Gpt4_1Mini(BaseLLM):
    def __init__(self):
        self.model = "openai/gpt-4.1-mini"
        self.base_url = "https://models.github.ai/inference"
        self.llm = ChatOpenAI(
            model=self.model,
            openai_api_base=self.base_url,
            openai_api_key=os.environ.get("GITHUB_TOKEN"),
            temperature=0.7
        )
        super().__init__(model=self.llm)

class Phi4(BaseLLM):
    def __init__(self):
        self.model = "microsoft/Phi-4-reasoning"
        self.base_url = "https://models.github.ai/inference"
        self.llm = ChatOpenAI(
            model=self.model,
            openai_api_base=self.base_url,
            openai_api_key=os.environ.get("GITHUB_TOKEN"),
            temperature=0.7
        )
        super().__init__(model=self.llm)

class Mistral(BaseLLM):
    def __init__(self):
        self.model = "mistral-ai/mistral-medium-2505"
        self.base_url = "https://models.github.ai/inference"
        self.llm = ChatOpenAI(
            model=self.model,
            openai_api_base=self.base_url,
            openai_api_key=os.environ.get("GITHUB_TOKEN"),
            temperature=0.7
        )
        super().__init__(model=self.llm)