from langchain_groq import ChatGroq
from dotenv import load_dotenv
from chatbot.Tools.tools import tools
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
import os
load_dotenv()


class GroqLLM:
    def __init__(self):
        self.llm = ChatGroq(model='gemma2-9b-it', api_key=os.getenv('GROQ_API_KEY'))
        self.prompt = ChatPromptTemplate.from_messages(
            [
                ("system", "{system}"),
                MessagesPlaceholder("messages")
            ]
        )


    def get_llm_without_tools(self):
        chain = self.prompt | self.llm
        return chain

    def get_llm_with_tools(self):
        chain = self.prompt | self.llm.bind_tools(tools)
        return chain