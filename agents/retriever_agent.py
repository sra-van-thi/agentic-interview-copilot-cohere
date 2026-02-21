def retriever_agent(state):
    docs = state["vectorstore"].similarity_search(state["question"], k=4)
    state["context"] = "\n".join(d.page_content for d in docs)
    return state
