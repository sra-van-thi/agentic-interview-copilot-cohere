from langchain_openai import ChatOpenAI
import os
from langgraph.graph import StateGraph
from agents.answer_evaluator_agent import answer_evaluator_agent
from agents.final_decision_agent import final_decision_agent

def build_evaluation_graph(api_key: str):
    answer_evaluator_agent.api_key = api_key
    final_decision_agent.api_key = api_key

    graph = StateGraph(dict)
    graph.add_node("evaluate", answer_evaluator_agent)
    graph.add_node("decision", final_decision_agent)

    graph.set_entry_point("evaluate")
    graph.add_edge("evaluate", "decision")
    graph.set_finish_point("decision")

    return graph.compile()
