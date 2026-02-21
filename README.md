
py -3.11 -m venv Ivenv
Ivenv\Scripts\activate
python --version

pip install -r requirements.txt
uvicorn api.main:app --reload
streamlit run ui/app.py

###
Add git Repo