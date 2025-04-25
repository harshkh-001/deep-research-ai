# 🧠 Deep Research AI Agentic System

A dual-agent LLM-powered system that automates deep research and answer synthesis using real-time web search and a modular LangGraph-based agent workflow.

## 📌 Features

- 🌐 **Real-time Search** with Tavily API
- 🔄 **Stateful Workflow** using LangGraph
- 🧩 **Modular Agents** for Research and Answer Drafting
- 📚 **Cited Answers** for transparency
- 📎 **Prompt Templates** for consistent responses

---

## 🏗️ Project Structure

```
deep-research-ai/
│
├── agents/
│   ├── researcher_agent.py          # Handles Tavily search and parsing
│   └── answer_drafter_agent.py      # Handles response drafting via LangChain
│
├── workflows/
│   └── main_graph.py                # Defines the LangGraph workflow (nodes, transitions)
│
├── prompts/
│   └── template.txt                 # Prompt template used for the LLM
│
├── main.py                          # CLI entry point
├── .env.example                     # Sample for API keys
├── requirements.txt                 # Python dependencies
└── README.md                        # Project documentation
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/harshkh-001/deep-research-ai
cd deep-research-ai
```

# 🧠 Steps to Get Ollama Running on Windows

## 1. Install Ollama

If you haven’t installed Ollama yet:

👉 [Download Ollama for Windows](https://ollama.com/download)

Follow the installer instructions to complete the setup.

---

## 2. Start the Ollama Server

Open a new terminal (PowerShell or Command Prompt), then run:

```bash
ollama run llama2:7b


### 2. Set Up Environment

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file and add:

```
TAVILY_API_KEY=your_tavily_key
```

### 3. Run the System

```bash
python main.py
```

You'll be prompted to enter a research topic. The system will:
- Search the web
- Summarize and synthesize a detailed answer
- Output the final result with citations

---

## 💡 Example

**Input:**  
```bash
What are the recent breakthroughs in quantum cryptography?
```

**Output (trimmed):**
```
Quantum cryptography has recently seen developments such as ...  
Sources:  
1. https://arxiv.org/abs/xyz  
2. https://techcrunch.com/article/quantum-advancement/
```

---

## 🧠 Architecture Overview

- **Agent 1: Research Agent**  
  Uses Tavily to fetch relevant search results, filters and preprocesses the content.

- **Agent 2: Answer Drafter**  
  Uses LangChain with prompt templates to generate human-like answers with citations.

- **LangGraph Workflow**  
  Handles transitions and fallback between agents to ensure robustness.

---

## 🧪 Tech Stack

- Python 3.11+
- LangChain + LangGraph
- Tavily API
- Ollama (llama2:7b)
- Typer (CLI)
- Rich (output formatting)

---

## 📂 Modularity

You can easily replace:
- llama2:7b with any LLM (GPT-4, Claude, Mistral, etc.)
- CLI with FastAPI or Streamlit frontend

---

## 📬 Contact

**GitHub:** [harshkh-001](https://github.com/harshkh-001)  
**Email:** harshkhandelwal1245@gmail.com

---

