from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import random

app = FastAPI()

# ✅ CORS FIX (CRITICAL)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class AnswerRequest(BaseModel):
    answer: str

@app.post("/analyze-answer")
def analyze_answer(req: AnswerRequest):
    score = random.randint(60, 90)
    confidence = random.choice(["Low", "Medium", "High"])

    return {
        "score": score,
        "confidence": confidence,
        "feedback": "Good structure, improve clarity and confidence."
    }
HR_QUESTIONS = [
    "Tell me about yourself.",
    "What are your strengths and weaknesses?",
    "Why should we hire you?",
    "Explain a challenging situation you handled.",
    "Where do you see yourself in 5 years?"
]

@app.get("/get-question")
def get_question():
    return {
        "question": random.choice(HR_QUESTIONS)
    }
