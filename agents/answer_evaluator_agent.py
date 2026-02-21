from langchain_community.chat_models import ChatCohereAPI

llm = ChatCohereAPI(model="command-r-plus")

def answer_evaluator_agent(state):
    prompt = f"""
Rate each answer (1-10) based on depth and experience.

Answers:
{state["answers"]}

Return STRICT JSON:
{{"ratings": {{}}}}
"""
    state["ratings"] = llm.invoke(prompt).content
    return state
