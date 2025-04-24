from typing import TypedDict, List

class ResearchState(TypedDict):
    topic: str
    search_results: List[str]
    summary: str
