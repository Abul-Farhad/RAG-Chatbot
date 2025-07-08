from langgraph.graph.message import add_messages
from typing_extensions import TypedDict, List, Annotated
from langchain_core.messages import BaseMessage

class State(TypedDict):
    """Represent the structure of the state used in the graph workflow."""
    messages: Annotated[List[BaseMessage], add_messages]
    summary: str