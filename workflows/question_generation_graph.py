from langgraph.graph import StateGraph
from agents.retriever_agent import retriever_agent
from agents.skill_extractor_agent import skill_extractor_agent
from agents.skill_question_agent import skill_question_agent

def build_question_graph(api_key: str):
    retriever_agent.api_key = api_key
    skill_extractor_agent.api_key = api_key
    skill_question_agent.api_key = api_key

    graph = StateGraph(dict)
    graph.add_node("retrieve", retriever_agent)
    graph.add_node("extract", skill_extractor_agent)
    graph.add_node("questions", skill_question_agent)

    graph.set_entry_point("retrieve")
    graph.add_edge("retrieve", "extract")
    graph.add_edge("extract", "questions")
    graph.set_finish_point("questions")

    return graph.compile()
