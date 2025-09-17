# 🤖 LangGraph Agent Learning Project

A comprehensive step-by-step journey through building intelligent AI agents using LangGraph, from basic chatbots to advanced multi-agent systems with tools, memory, human-in-the-loop workflows, and time travel capabilities.

## 📋 Table of Contents

- [Project Overview](#project-overview)
- [Learning Path](#learning-path)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Agent Implementations](#agent-implementations)
- [Key Features](#key-features)
- [Usage Examples](#usage-examples)
- [Environment Setup](#environment-setup)
- [Technologies Used](#technologies-used)
- [Learning Outcomes](#learning-outcomes)
- [Next Steps](#next-steps)
- [Contributing](#contributing)

## 🎯 Project Overview

This repository contains a complete learning journey through LangGraph agent development, progressing from manual implementations to prebuilt solutions. Each agent folder represents a different learning milestone, building upon previous concepts.

### Learning Philosophy
- **Manual Implementation First**: Understanding core concepts by building from scratch
- **Progressive Complexity**: Each agent adds new capabilities
- **Clean Architecture**: Modular design with separation of concerns
- **Production Ready**: Professional patterns suitable for real-world applications

## 🛤️ Learning Path

### Phase 1: Custom Workflow Mastery
1. **[Basic Chatbot](./first-agent/)** - Foundation with StateGraph and memory
2. **[Tool Integration](./second-agent/)** - Adding calculator and web search tools
3. **[Memory Management](./third-agent/)** - Persistent conversation memory
4. **[Human-in-the-Loop](./human-agent/)** - Interactive approval workflows
5. **[Custom State](./custom-state-agent/)** - Structured data management
6. **[Time Travel](./time-travel-agent/)** - Checkpoint navigation and replay

### Phase 2: Prebuilt Excellence
7. **[Prebuilt Agent](./prebuilt-agent/)** - Using `create_react_agent` for rapid development

## 📁 Project Structure

```
langgraph-agents/
├── README.md
├── .gitignore
├── requirements.txt
├── .env.example
├── first-agent/          # Basic chatbot
│   ├── state.py
│   ├── node.py
│   ├── graph.py
│   └── agent.py
├── second-agent/         # Tools integration
│   ├── state.py
│   ├── node.py          # Calculator + Web search
│   ├── graph.py
│   └── agent.py
├── third-agent/          # Memory persistence
├── human-agent/          # Human-in-the-loop
├── custom-state-agent/   # Custom state management
├── time-travel-agent/    # Checkpoint navigation
└── prebuilt-agent/       # Simple prebuilt implementation
    └── simple_agent.py   # One-file solution
```

## 🔧 Prerequisites

- Python 3.8+
- Basic understanding of Python programming
- API keys for external services (Google AI, Tavily)
- Git for version control

## 🚀 Installation

1. **Clone the repository**
   ```
   git clone https://github.com/yourusername/langgraph-agents.git
   cd langgraph-agents
   ```

2. **Create virtual environment**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```
   pip install -r requirements.txt
   ```

4. **Setup environment variables**
   ```
   cp .env.example .env
   # Edit .env with your API keys
   ```

## 🤖 Agent Implementations

### 1. Basic Chatbot (`first-agent/`)
**Core Concepts:** StateGraph, Messages, Memory
- Simple conversational interface
- In-memory persistence with MemorySaver
- Thread-based conversation management

### 2. Tool-Enhanced Agent (`second-agent/`)
**Core Concepts:** Tool Integration, Conditional Edges
- Calculator tool with Pydantic validation
- Web search integration with Tavily
- Automatic tool selection by LLM

### 3. Memory Agent (`third-agent/`)
**Core Concepts:** Persistent Memory, Thread Management
- Conversation history across sessions
- Memory inspection utilities
- Multi-thread conversation isolation

### 4. Human-in-the-Loop Agent (`human-agent/`)
**Core Concepts:** Interrupts, Command Objects, Approval Workflows
- Pause execution for human input
- Resume with human feedback
- Perfect for approval-required operations

### 5. Custom State Agent (`custom-state-agent/`)
**Core Concepts:** Structured State, Data Validation
- Custom state fields beyond messages
- Tool-driven state updates
- Structured data persistence

### 6. Time Travel Agent (`time-travel-agent/`)
**Core Concepts:** Checkpoints, State History, Replay
- Navigate conversation history
- Resume from any checkpoint
- Alternative outcome exploration

### 7. Prebuilt Agent (`prebuilt-agent/`)
**Core Concepts:** create_react_agent, Rapid Development
- All features in minimal code
- Production-ready patterns
- Easy customization and deployment

## ⭐ Key Features

### Manual Implementation Features
- **Modular Architecture**: Clean separation of state, nodes, graph, and interface
- **Type Safety**: Full Pydantic and TypedDict integration
- **Professional Patterns**: Industry-standard code organization
- **Educational Value**: Understanding of underlying mechanisms

### Prebuilt Implementation Features
- **Rapid Development**: Complete agent in 30 lines of code
- **Built-in Robustness**: Error handling, parallel execution, memory management
- **Advanced Capabilities**: ReAct patterns, structured output, dynamic prompts
- **Production Ready**: Scalable and maintainable from day one

## 💡 Usage Examples

### Running Basic Chatbot
```
cd first-agent
python agent.py
```

### Running Tool-Enhanced Agent
```
cd second-agent
python agent.py
```
**Try:** "Calculate 25 * 4 and then search for Python tutorials"

### Running Human-in-the-Loop Agent
```
cd human-agent
python agent.py
```
**Try:** "I need expert advice on AI ethics"

### Running Prebuilt Agent
```
cd prebuilt-agent
python simple_agent.py
```

## 🔐 Environment Setup

Create a `.env` file with the following variables:

```
# Google AI
GOOGLE_API_KEY=your_google_ai_api_key_here

# Tavily Search
TAVILY_API_KEY=your_tavily_api_key_here

# Optional: Other service keys
ANTHROPIC_API_KEY=your_anthropic_key_here
OPENAI_API_KEY=your_openai_key_here
```

## 🛠️ Technologies Used

- **[LangGraph](https://langchain-ai.github.io/langgraph/)** - Agent orchestration framework
- **[LangChain](https://python.langchain.com/)** - LLM application framework
- **[Google AI](https://ai.google/)** - Gemini 2.5 Flash model
- **[Tavily](https://tavily.com/)** - Web search API
- **[Pydantic](https://pydantic.dev/)** - Data validation and settings
- **[Python-dotenv](https://pypi.org/project/python-dotenv/)** - Environment variable management

## 🎓 Learning Outcomes

By completing this project, you'll master:

### Core Concepts
- StateGraph architecture and design patterns
- Message-based communication systems
- Tool integration and automatic selection
- Memory management and persistence strategies

### Advanced Techniques
- Human-in-the-loop workflow design
- Custom state management with structured data
- Checkpoint-based time travel and replay
- Error handling and recovery patterns

### Production Skills
- Professional code organization and modularity
- Type safety and validation with Pydantic
- Environment management and security
- Scalable agent architecture design

### Framework Expertise
- Manual LangGraph implementation vs. prebuilt solutions
- When to use custom workflows vs. create_react_agent
- Performance optimization and best practices
- Integration with external APIs and services

## 🚀 Next Steps

### Immediate Extensions
- **Database Integration**: Replace MemorySaver with PostgreSQL
- **FastAPI Integration**: Create REST API endpoints
- **Authentication**: Add user management and security
- **Deployment**: Docker containers and cloud deployment

### Advanced Projects
- **Multi-Agent Systems**: Orchestrate multiple specialized agents
- **RAG Integration**: Add document retrieval and knowledge bases
- **Streaming Responses**: Real-time response generation
- **Production Monitoring**: Logging, metrics, and observability

### Learning Resources
- [LangGraph Documentation](https://langchain-ai.github.io/langgraph/)
- [LangGraph Templates](https://github.com/langchain-ai/langgraph-templates)
- [Agent Architecture Patterns](https://python.langchain.com/docs/tutorials/agents/)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

### Development Setup
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **LangChain Team** for the incredible LangGraph framework
- **Google AI** for the Gemini models
- **Tavily** for the web search API
- **Open Source Community** for continuous inspiration

---

⭐ **Star this repository if you found it helpful in your LangGraph learning journey!**
```
