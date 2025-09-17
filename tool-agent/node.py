from langchain.chat_models import init_chat_model
from langchain_tavily import TavilySearch
from langchain_core.tools import tool
from pydantic import BaseModel, Field
from .state import State
from dotenv import load_dotenv

load_dotenv()

llm = init_chat_model("google_genai:gemini-2.5-flash")

web_search_tool = TavilySearch(max_result=2)

class CalculatorInput(BaseModel):
    number1: float = Field(description="first number for the calculation")
    number2: float = Field(description="second number for the calculation")
    operation: str = Field(description="Operation to perform: +,-,*,/")

@tool
def calculator_tool(number1:float, number2:float,operation: str) -> float:
    """Perform mathematical calculations between two numbers.
    
    Args:
        number1: First number
        number2: Second number  
        operation: Mathematical operation (+, -, *, /)
    
    Returns:
        Result of the calculation
    """

    if operation == "+":
        return number1 + number2
    elif operation == "-":
        return number1 - number2
    elif operation == "*":
        return number1 * number2
    elif operation == "/":
        if number2 == 0:
            return "Error: Division by zero"
        return number1 / number2
    else:
        return "Error: Invalid operation. Use +, -, *, or /"

tools = [web_search_tool,calculator_tool]

llm_with_tools = llm.bind_tools(tools)

def chatbot(state:State):
    return {"messages":[llm_with_tools.invoke(state["messages"])]}
