from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

def skill_extractor_agent(state):
    prompt = f"""
Extract technical skills from the resume below.

Resume:
{state["context"]}

Return STRICT JSON:
{{"skills": {{"GenAI":[], "Cloud":[], "Programming":[], "DevOps":[]}}}}
"""
    state["skills"] = llm.invoke(prompt).content
    return state
