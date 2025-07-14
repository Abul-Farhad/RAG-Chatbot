import os
from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from chatbot.Tools.tools import tools

load_dotenv()

class BaseLLM:
    def __init__(self, model = None):
        self.llm = model
        self.prompt = ChatPromptTemplate.from_messages(
            [
                # ("system", "{system}. Respond to the user **only in Bangla**."),
                ("system", "{system}"),
                ("system", "Here is the user information: {user_information}"),

                MessagesPlaceholder("messages"),

            ]
        )

    def get_llm_without_tools(self):
        chain = self.prompt | self.llm
        return chain

    def get_llm_with_tools(self):
        chain = self.prompt | self.llm.bind_tools(tools)
        return chain