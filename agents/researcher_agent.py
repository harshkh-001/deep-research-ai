from langchain_community.tools.tavily_search import TavilySearchResults
from langchain.agents import Tool, AgentExecutor, initialize_agent
from langchain_community.llms import Ollama
from dotenv import load_dotenv
load_dotenv()

def get_research_agent():
    llm = Ollama(model="llama2:7b", temperature=0)
    search = TavilySearchResults(max_results=5)

    tools = [
        Tool(
            name="TavilySearch",
            func=search.run,
            description="Search the web for up-to-date information"
        )
    ]

    agent = initialize_agent(
        tools,
        llm,
        agent="zero-shot-react-description",
        verbose=True
    )
    return agent
