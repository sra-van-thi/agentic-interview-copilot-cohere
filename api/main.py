import os, shutil
from dotenv import load_dotenv


load_dotenv()
COHERE_API_KEY = os.getenv("COHERE_API_KEY")
print(f"OCOHERE_API_KEY: {COHERE_API_KEY}")
if not COHERE_API_KEY:
    raise ValueError("COHERE_API_KEY not set. Please check .env file!")

from fastapi import FastAPI, UploadFile, File, HTTPException
from rag.ingest import ingest   
from workflows.question_generation_graph import build_question_graph
from workflows.evaluation_graph import build_evaluation_graph

UPLOAD_DIR = "data/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

app = FastAPI()
vectorstore = None

question_graph = build_question_graph(api_key=COHERE_API_KEY)
evaluation_graph = build_evaluation_graph(api_key=COHERE_API_KEY)

@app.post("/upload-resume")
def upload_resume(file: UploadFile = File(...)):
    global vectorstore
    path = os.path.join(UPLOAD_DIR, file.filename)
    with open(path, "wb") as f:
        shutil.copyfileobj(file.file, f)

    vectorstore = ingest(UPLOAD_DIR)
    return {"message": "Resume uploaded"}

@app.get("/generate-questions")
def generate_questions():
    if not vectorstore:
        raise HTTPException(400, "Upload resume first")

    state = {"question": "Extract skills", "vectorstore": vectorstore}
    result = question_graph.invoke(state)
    return result["questions"]

@app.post("/evaluate-interview")
def evaluate(payload: dict):
    result = evaluation_graph.invoke({"answers": payload["answers"]})
    return result["final_report"]
