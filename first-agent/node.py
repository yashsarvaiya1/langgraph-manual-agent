from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from .state import State

load_dotenv()

llm = init_chat_model("google_genai:gemini-2.5-flash")

def chatbot(state: State):
    return {"messages": [llm.invoke(state["messages"])]}
