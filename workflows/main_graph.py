from langgraph.graph import StateGraph
from agents.researcher_agent import get_research_agent
from agents.answer_drafter_agent import draft_answer
from .state import ResearchState


def build_workflow():
    agent = get_research_agent()

    def research_step(state):
        query = state["topic"]
        response = agent.run(query)
        return {"topic": query, "context": response}

    def answer_step(state):
        context = state["context"]
        answer = draft_answer(context)
        return {"final_answer": answer}

    graph = StateGraph(ResearchState)
    graph.add_node("research", research_step)
    graph.add_node("draft", answer_step)
    graph.set_entry_point("research")
    graph.add_edge("research", "draft")
    graph.set_finish_point("draft")

    return graph.compile()
