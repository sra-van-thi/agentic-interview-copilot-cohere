import streamlit as st, requests

API = "http://localhost:8000"

st.title("🤖 Agentic Interview Copilot")

file = st.file_uploader("Upload Resume", type=["pdf","docx","txt"])
if file:
    requests.post(f"{API}/upload-resume", files={"file": file})
    st.success("Resume uploaded")

if st.button("Generate Questions"):
    
    respose = requests.get(f"{API}/generate-questions").json()
    st.session_state.qs=respose.json()
    st.success("Questions generated")
answers = {}
if "qs" in st.session_state:
    qs_data = st.session_state.qs

    # Validate structure
    if not isinstance(qs_data, dict):
        st.error(f"Unexpected response format: {type(qs_data)}")
        st.write(qs_data)
    else:
        for skill, lvls in st.session_state.qs.items():
            st.subheader(skill)

             # Validate lvls is a dictionary
            if not isinstance(lvls, dict):
                st.warning(f"Unexpected format for {skill}: {type(lvls)}")
                continue

            for lvl, qs in lvls.items():
                if isinstance(qs, list):
                    for q in qs:
                        answers[q] = st.text_area(q)
                else:
                    st.warning(f"Expected list for {skill}/{lvl}, got {type(qs)}")
if st.button("Submit Interview"):
    res = requests.post(f"{API}/evaluate-interview", json={"answers": answers})
    st.json(res.json())
