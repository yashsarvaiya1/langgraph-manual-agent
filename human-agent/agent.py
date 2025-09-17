from langchain_core.messages import HumanMessage
from langgraph.types import Command
from .graph import graph

def stream_response(user_input: str, thread_id: str = "default"):
    config = {"configurable": {"thread_id": thread_id}}
    for event in graph.stream({"messages": [HumanMessage(content=user_input)]}, config):
        for value in event.values():
            if "messages" in value:  # Check if messages exist
                value["messages"][-1].pretty_print()

# "What should I do about my personal relationship issues?"
# "Help me make a difficult business decision"
# "I need advice on career changes - can you get human input?"
# "What's the best approach for my specific situation?"

def resume_with_human_input(human_input: str, thread_id: str = "default"):
    config = {"configurable": {"thread_id": thread_id}}
    human_command = Command(resume={"data": human_input})
    for event in graph.stream(human_command, config):
        for value in event.values():
            if "messages" in value:  # Check if messages exist
                value["messages"][-1].pretty_print()

if __name__ == "__main__":
    print("🤖 Human-in-the-Loop Agent Started")
    
    while True:
        user_input = input("\n💬 You: ")
        if user_input.lower() in ["quit", "exit", "q"]:
            print("👋 Goodbye!")
            break
        
        print("🤖 Agent:")
        stream_response(user_input, "main")
        
        # Check if interrupted
        state = graph.get_state({"configurable": {"thread_id": "main"}})
        if state.next:  # Execution paused
            print("⏸️  Agent paused - needs human input")
            human_response = input("🧑 Your response: ")
            print("🤖 Agent continuing:")
            resume_with_human_input(human_response, "main")
