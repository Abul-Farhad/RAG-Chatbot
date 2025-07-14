from langchain_core.messages import HumanMessage, RemoveMessage
from chatbot.State.state import State, get_size_in_kb
from chatbot.LLM.githubLLM import Gpt4_1Mini
from chatbot.LLM.groqLLM import LLama3, MistralSaba24b,DeepseekR1
class AgentNode:
    def __init__(self):
        self.llm_without_tools = DeepseekR1().get_llm_without_tools()
        self.llm_with_tools = DeepseekR1().get_llm_with_tools()

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
- Always follow the instructions carefully. You can use tools when appropriate.
- When the user asks about smartphones, use the `retrieve_smartphone_data` tool. Note that all smartphone prices are in BDT (Bangladeshi Taka).
- Only create an issue if the user explicitly requests it.
- If the user encounters a problem or you don’t have the necessary access to complete a task, politely ask if they would like to create an issue for it.
- If an issue has already been created, apologize for the inconvenience and confirm that the issue has been successfully submitted. Be sure to mention the issue title in your response."""
        summary = state.get("summary", "")
        if summary:
            system_message += f"Summary of the conversation so far: {summary}\n"

        user_information = state.get("user_information", {})
        response = self.llm_with_tools.invoke({"system": system_message, "messages": state["messages"], "user_information": user_information})
        print("Current state size in KB: ", get_size_in_kb(state))
        return {"messages": [response]}

class SummarizerNode:
    def __init__(self):
        self.llm_without_tools = LLama3().get_llm_without_tools()
        self.llm_with_tools = LLama3().get_llm_with_tools()

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
