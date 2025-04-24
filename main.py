from workflows.main_graph import build_workflow

if __name__ == "__main__":
    graph = build_workflow()
    user_query = input("Enter your research topic: ")
    result = graph.invoke({"topic": user_query})
    print("\n📄 Final Answer:\n", result["final_answer"])