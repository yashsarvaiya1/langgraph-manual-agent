from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.prebuilt import ToolNode, tools_condition
from .node import chatbot, tools
from .state import State

def generate_graph():
    memory = InMemorySaver()
    graph_builder = StateGraph(State)
    graph_builder.add_node("chatbot", chatbot)
    graph_builder.add_node("tools", ToolNode(tools=tools))
    graph_builder.add_edge(START, "chatbot")
    graph_builder.add_conditional_edges("chatbot", tools_condition, {"tools": "tools", END: END})
    graph_builder.add_edge("tools", "chatbot")
    return graph_builder.compile(checkpointer=memory)

graph = generate_graph()
