from langchain_core.messages import HumanMessage
from langgraph.types import Command
from .graph import graph

def chat(user_input: str, thread_id: str = "main"):
    """Simple chat function"""
    config = {"configurable": {"thread_id": thread_id}}
    
    for event in graph.stream({"messages": [HumanMessage(content=user_input)]}, config):
        for value in event.values():
            if "messages" in value:
                value["messages"][-1].pretty_print()
    
    # Check if we need human input
    state = graph.get_state(config)
    if state.next:  # Agent is waiting
        print("⏸️  Agent needs human verification")
        
        # Simple yes/no verification
        correct = input("Is the information correct? (y/n): ")
        
        if correct.lower().startswith('y'):
            response = {"correct": "yes"}
        else:
            name = input("Correct name: ")
            birthday = input("Correct birthday: ")
            response = {"correct": "no", "name": name, "birthday": birthday}
        
        # Resume with response
        for event in graph.stream(Command(resume=response), config):
            for value in event.values():
                if "messages" in value:
                    value["messages"][-1].pretty_print()

def show_state(thread_id: str = "main"):
    """Show what's stored in state"""
    config = {"configurable": {"thread_id": thread_id}}
    state = graph.get_state(config)
    
    print(f"Name: {state.values.get('name', 'Not set')}")
    print(f"Birthday: {state.values.get('birthday', 'Not set')}")

if __name__ == "__main__":
    print("🤖 Custom State Agent")
    print("Try: 'Look up when Python was created and verify it'")
    
    while True:
        user_input = input("\n💬 You: ")
        
        if user_input.lower() in ["quit", "exit"]:
            print("👋 Goodbye!")
            break
        elif user_input.lower() == "state":
            show_state()
        else:
            chat(user_input)
