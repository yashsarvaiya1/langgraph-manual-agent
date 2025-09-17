from langchain.chat_models import init_chat_model
from langchain_core.tools import tool
from dotenv import load_dotenv
from .state import State
from langgraph.types import interrupt


load_dotenv()

llm = init_chat_model("google_genai:gemini-2.5-flash")

@tool
def human_assistance(query: str) -> str:
    """ALWAYS use this tool when the user explicitly asks for human help, expert advice, or human assistance.
    
    Use this tool when:
    - User says "I need expert advice"
    - User says "ask a human" 
    - User says "get human help"
    - User requests human guidance on any topic
    - Complex problems requiring human expertise
    
    Args:
        query: The question or problem to ask the human expert
    """
    human_response = interrupt({"query":query})
    return human_response["data"]

tools = [human_assistance]

llm_with_tools = llm.bind_tools(tools=tools)

def chatbot(state: State):
    message = llm_with_tools.invoke(state["messages"])
    assert len(message.tool_calls) <= 1
    return {"messages": [message]}
