from langgraph.graph import StateGraph, START, END

from chatbot.Nodes.nodes import AgentNode
from chatbot.State.state import State


class Graph:
    """
    A class to build and compile a state graph for an agentic AI workflow.
    """

    def __init__(self, model):
        self.llm = model
        self.graph_builder = StateGraph(State)

    def setup_graph(self):
        """
        Set up the graph with a basic chatbot node.
        """

        self.agent_node = AgentNode(self.llm)
        self.graph_builder.add_node("agent", self.agent_node.get_agent)
        self.graph_builder.add_edge(START, "agent")
        self.graph_builder.add_edge("agent", END)

        return self.graph_builder.compile()


