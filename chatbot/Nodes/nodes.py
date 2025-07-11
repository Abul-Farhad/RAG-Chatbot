from langchain_core.messages import HumanMessage, RemoveMessage
from chatbot.LLM.groqLLM import GroqLLM
from chatbot.State.state import State

class AgentNode:
    def __init__(self):
        self.llm_without_tools = GroqLLM().get_llm_without_tools()
        self.llm_with_tools = GroqLLM().get_llm_with_tools()

    def get_agent(self, state: State) -> dict:
        """
        Retrieve the agent's response based on the current state.

        Args:
            state (State): The current state containing messages.

        Returns:
            dict: A dictionary containing the agent's response.
        """
        print("--- Agent Node Called ---")
        system_message = f"""You are Shoppio, an AI assistant designed to help users with their shopping-related needs.
Use tool retrieve_smartphone_data, if user asked about smartphones. The smartphone prices are in Bdt.
Create an issue only when the user explicitly requests it.
If the user encounters a problem or you lack the necessary access to perform a task, politely ask if they would like to create an issue for it.
If an issue has already been created, apologize for the inconvenience and confirm that the issue has been successfully created. Include the issue title in your response."""
#         system_message = f"""Your name is Shoppio, an AI assistant designed to help users with their shopping needs.
# Do not create issue regarding greetings, farewells, or other non-shopping related topics.
# Create issue only if the user explicitly asks for it .
# If you do not have any access for any functionality or the user is facing trouble, politely ask whether the user want to create that as an issue or not.
# If you found any issue has been created, apology to the user for that problem and tell the issue is successfully created with title"""
        summary = state.get("summary", "")
        if summary:
            system_message += f"Summary of the conversation so far: {summary}\n"

        user_information = state.get("user_information", {})
        response = self.llm_with_tools.invoke({"system": system_message, "messages": state["messages"], "user_information": user_information})
        return {"messages": [response]}

class SummarizerNode:
    def __init__(self):
        self.llm_without_tools = GroqLLM().get_llm_without_tools()
        self.llm_with_tools = GroqLLM().get_llm_with_tools()

    def get_summarizer(self, state: State) -> dict:
        """
        Summarize the conversation based on the current state.

        Args:
            state (State): The current state containing messages.

        Returns:
            dict: A dictionary containing the summary of the conversation.
        """
        print("--- Summarizer Node Called ---")
        system_message = f"""You are a summarizer that condenses the conversation into a concise summary."""
        summary = state.get("summary", "")
        summary = state.get("summary", "")
        if summary:
            summary_message = (
                f"This is summary of the conversation to date: {summary}\n\n"
                "Extend the summary by taking into account the new messages above:"
            )
        else:
            summary_message = "Create a summary of the conversation above:"
        user_information = state.get("user_information", {})
        response = self.llm_without_tools.invoke({"system": system_message, "messages": state["messages"] + [HumanMessage(content=summary_message)], "user_information": user_information})
        delete_messages = [RemoveMessage(id=m.id) for m in state["messages"][:-2]]
        print("delete_messages:", delete_messages)
        return {"messages": delete_messages, "summary": response.content}
