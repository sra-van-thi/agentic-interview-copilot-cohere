import json
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini")

def skill_question_agent(state):
    prompt = f"""
Generate interview questions at L1/L2/L3 levels.

Skills:
{state["skills"]}

Return STRICT JSON:
{{"questions": {{"Skill": {{"L1":[], "L2":[], "L3":[]}}}}}}
"""
    response = llm.invoke(prompt).content
    
    try:
        parsed_response = json.loads(response)
        state["questions"] = parsed_response.get("questions", {})
    except json.JSONDecodeError:
        raise ValueError(f"LLM response is not valid JSON: {response}")
    
    return state
