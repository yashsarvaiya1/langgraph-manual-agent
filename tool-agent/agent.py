from langchain_core.messages import HumanMessage
from .graph import graph

def stream_response(user_input:str, thread_id:str = "default"):
    config = {"configurable": {"thread_id":thread_id}}
    for event in graph.stream({"messages":[HumanMessage(content=user_input)]},config):
        for value in event.values():
            value["messages"][-1].pretty_print()

if __name__ == "__main__":
    print("Ai Started:")

    while True:
        user_input = input("\n💬 You: ")
        if user_input.lower() in ["quit", "exit", "q"]:
            print("👋 Goodbye!")
            break
        
        print("🤖 Agent:")
        stream_response(user_input, "interactive")
        user_input = input("\n💬 You: ")
        if user_input.lower() in ["quit", "exit", "q"]:
            print("👋 Goodbye!")
            break
        
        print("🤖 Agent:")
        stream_response(user_input, "interactive")
    
