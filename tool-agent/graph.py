from langgraph.graph import StateGraph,START,END
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt.tool_node import ToolNode,tools_condition
from .node import chatbot,tools
from .state import State

def generate_graph():
    memory = MemorySaver()
    gb = StateGraph(State)

    gb.add_node("chatbot",chatbot)
    tool_node = ToolNode(tools=tools)

    gb.add_node("tools",tool_node)

    gb.add_edge(START,"chatbot")
    gb.add_conditional_edges(
        "chatbot",tools_condition,
        {"tools":"tools", END:END}
    )

    gb.add_edge("tools","chatbot")

    return gb.compile(checkpointer=memory)

graph = generate_graph()
    
