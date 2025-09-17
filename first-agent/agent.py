from langchain_core.messages import HumanMessage
from .graph import graph

def stream_response(user_input:str, thread_id:str = "default"):
    config = {"configurable": {"thread_id":thread_id}}
    human_message = HumanMessage(content=user_input)
    for event in graph.stream({"messages":[human_message]},config):
        for value in event.values():
            value["messages"][-1].pretty_print()
    
if __name__ == "__main__":
    print("Ai sstarted:")

    while True:
        user_input = input("you: ")
        if(user_input.lower() in ["quit","exit"] ):
            print("goodbye")
            break
        stream_response(user_input,"yash")

