from langchain_core.messages import HumanMessage
from .graph import graph

def chat(user_input: str, thread_id: str = "main"):
    """Simple chat function"""
    config = {"configurable": {"thread_id": thread_id}}
    
    for event in graph.stream({"messages": [HumanMessage(content=user_input)]}, config):
        for value in event.values():
            if "messages" in value:
                value["messages"][-1].pretty_print()

def show_history(thread_id: str = "main"):
    """Show conversation history with checkpoints"""
    config = {"configurable": {"thread_id": thread_id}}
    
    print(f"📜 History for Thread: {thread_id}")
    print("=" * 50)
    
    states = []
    for i, state in enumerate(graph.get_state_history(config)):
        states.append(state)
        print(f"{i+1}. Messages: {len(state.values['messages'])}, Next: {state.next}")
    
    return states

def time_travel(checkpoint_num: int = None, thread_id: str = "main"):
    """Travel back to a specific checkpoint and continue from there"""
    config = {"configurable": {"thread_id": thread_id}}
    
    # Get all states
    states = list(graph.get_state_history(config))
    
    if not states:
        print("❌ No history found")
        return
    
    if checkpoint_num is None:
        print("📜 Available checkpoints:")
        for i, state in enumerate(states):
            print(f"  {i+1}. Messages: {len(state.values['messages'])}, Next: {state.next}")
        checkpoint_num = int(input("\nSelect checkpoint number: "))
    
    if 1 <= checkpoint_num <= len(states):
        selected_state = states[checkpoint_num - 1]
        print(f"\n🕰️ Time traveling to checkpoint {checkpoint_num}")
        print(f"Config: {selected_state.config['configurable']['checkpoint_id']}")
        
        # Resume from this checkpoint
        for event in graph.stream(None, selected_state.config):
            for value in event.values():
                if "messages" in value:
                    value["messages"][-1].pretty_print()
    else:
        print("❌ Invalid checkpoint number")

if __name__ == "__main__":
    print("🤖 Time Travel Agent")
    print("Commands: 'history' = show checkpoints, 'travel' = time travel, 'quit' = exit")
    
    while True:
        user_input = input("\n💬 You: ")
        
        if user_input.lower() in ["quit", "exit"]:
            print("👋 Goodbye!")
            break
        elif user_input.lower() == "history":
            show_history()
        elif user_input.lower() == "travel":
            time_travel()
        else:
            chat(user_input)
