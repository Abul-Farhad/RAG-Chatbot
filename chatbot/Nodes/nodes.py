from chatbot.State.state import State


class AgentNode:
    def __init__(self, llm):
        self.llm = llm

    def get_agent(self, state: State) -> dict:
        """
        Retrieve the agent's response based on the current state.

        Args:
            state (State): The current state containing messages.

        Returns:
            dict: A dictionary containing the agent's response.
        """
        messages = state["messages"]
        response = self.llm.invoke(messages)
        return {"messages": [response]}

