from typing import Literal
from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode, tools_condition
from chatbot.Nodes.nodes import AgentNode, SummarizerNode
from chatbot.State.state import State
from chatbot.Tools.tools import tools


class Graph:
    """
    A class to build and compile a state graph for an agentic AI workflow.
    """

    def __init__(self):
        self.graph_builder = StateGraph(State)


    def setup_graph(self, checkpoint=None):
        """
        Set up the graph with a basic chatbot node.
        """

        def agent_conditions(state: State) -> str:
            # First check if tool needs to be called
            tool_result = tools_condition(state)
            if tool_result != END:
                return tool_result

            # Then check if summarizer should be called
            if len(state["messages"]) > 6:
                return "summarizer"

            # Otherwise, finish
            return END

        self.agent_node = AgentNode()
        self.summarizer_node = SummarizerNode()
        self.graph_builder.add_node("agent", self.agent_node.get_agent)
        self.graph_builder.add_node("summarizer", self.summarizer_node.get_summarizer)
        self.graph_builder.add_node("tools", ToolNode(tools))
        self.graph_builder.add_edge(START, "agent")
        self.graph_builder.add_conditional_edges(
            "agent",
            agent_conditions
        )
        self.graph_builder.add_edge("tools", "agent")
        self.graph_builder.add_edge("summarizer", END)
        if not checkpoint:
            return self.graph_builder.compile()
        return self.graph_builder.compile(checkpointer=checkpoint)


