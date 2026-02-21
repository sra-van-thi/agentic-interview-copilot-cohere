from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

def final_decision_agent(state):
    prompt = f"""
Based on ratings, decide:
Strong / Moderate / Reject

Ratings:
{state["ratings"]}

Return STRICT JSON:
{{
 "final_decision":"",
 "strong_skills":[],
 "weak_skills":[],
 "skill_summary":{{}}
}}
"""
    state["final_report"] = llm.invoke(prompt).content
    return state
