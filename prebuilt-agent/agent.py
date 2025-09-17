from dotenv import load_dotenv
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import InMemorySaver
from langchain.chat_models import init_chat_model
from langchain_tavily import TavilySearch
from pydantic import BaseModel

load_dotenv()

# Tools (same as before)
def calculator(number1: float, number2: float, operation: str) -> float:
    """Perform mathematical calculations"""
    if operation == "+": return number1 + number2
    elif operation == "-": return number1 - number2
    elif operation == "*": return number1 * number2
    elif operation == "/": return number1 / number2 if number2 != 0 else "Error: Division by zero"
    else: return "Error: Invalid operation"

web_search = TavilySearch(max_results=2)

# Configure LLM
model = init_chat_model("google_genai:gemini-2.5-flash", temperature=0)

# 🎯 CREATE AGENT IN ONE LINE!
agent = create_react_agent(
    model=model,
    tools=[calculator, web_search],
    checkpointer=InMemorySaver(),  # Built-in memory!
    prompt="You are a helpful AI assistant with access to calculator and web search tools."
)

# Simple chat function
def chat(user_input: str, thread_id: str = "main"):
    config = {"configurable": {"thread_id": thread_id}}
    response = agent.invoke(
        {"messages": [{"role": "user", "content": user_input}]}, 
        config
    )
    print(response["messages"][-1].content)

if __name__ == "__main__":
    print("🤖 Prebuilt Agent (Super Simple!)")
    
    while True:
        user_input = input("\n💬 You: ")
        if user_input.lower() in ["quit", "exit"]:
            print("👋 Goodbye!")
            break
        chat(user_input)
