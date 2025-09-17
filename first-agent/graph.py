from langgraph.graph import StateGraph,START,END
from langgraph.checkpoint.memory import MemorySaver
from .node import chatbot
from .state import State

def generate_graph():
    memory = MemorySaver()
    graph_builder = StateGraph(State)
    graph_builder.add_node("chatbot",chatbot)
    graph_builder.add_edge(START,"chatbot")
    graph_builder.add_edge("chatbot",END)
    return graph_builder.compile(checkpointer=memory)

graph = generate_graph()

