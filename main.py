from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()

qa_model = pipeline("text-generation", model="gpt2")

class Question(BaseModel):
    question: str


@app.post("/ask")
def ask_question(q: Question):
    response = qa_model(q.question, max_length=50)

    return {
        "answer": response[0]["generated_text"]
    }