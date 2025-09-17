from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
from langchain_core.tools import tool, InjectedToolCallId
from langchain_core.messages import ToolMessage
from langgraph.types import interrupt, Command
from typing import Annotated
from pydantic import BaseModel, Field
from .state import State

load_dotenv()

llm = init_chat_model("google_genai:gemini-2.5-flash")


@tool
def human_assistance(
    name: str, birthday: str, tool_id: Annotated[str, InjectedToolCallId]
) -> str:
    """Request human verification and update state with verified information."""
    human_response = interrupt(
        {
            "question": "is this correct?",
            "neme": name,
            "birthday": birthday,
        }
    )
    if human_response.get("correct", "").lower().startswith("y"):
        verified_name = name
        verified_birthday = birthday
        response = "Correct"
    else:
        verified_name = human_response.get("name", name)
        verified_birthday = human_response.get("birthday", birthday)
        response = f"Made a correction: {human_response}"

    # Update state from within tool
    state_update = {
        "name": verified_name,
        "birthday": verified_birthday,
        "messages": [ToolMessage(response, tool_call_id=tool_id)],
    }
    return Command(update=state_update)

tools = [human_assistance]
llm_with_tools = llm.bind_tools(tools)

def chatbot(state: State):
    message = llm_with_tools.invoke(state["messages"])
    assert len(message.tool_calls) <= 1
    return {"messages": [message]}


