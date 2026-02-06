from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import random

app = FastAPI(title="IntelliView AI Backend")

# ✅ CORS (required for frontend connection)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------
# Data Models
# -----------------------------
class AnswerRequest(BaseModel):
    answer: str


# -----------------------------
# Mock HR Question Bank
# -----------------------------
HR_QUESTIONS = [
    "Tell me about yourself.",
    "Why should we hire you?",
    "What are your strengths and weaknesses?",
    "Describe a challenge you overcame.",
    "Where do you see yourself in 5 years?"
]

@app.get("/get-question")
def get_question():
    return {"question": random.choice(HR_QUESTIONS)}


# -----------------------------
# Confidence & Nervousness Logic
# -----------------------------
def detect_nervousness(answer: str):
    fillers = ["uh", "um", "like", "maybe", "i think"]
    count = sum(answer.lower().count(f) for f in fillers)

    if count >= 3:
        return "High Nervousness"
    elif count == 2:
        return "Moderate Nervousness"
    else:
        return "Low Nervousness"


# -----------------------------
# MAIN ANALYSIS ENDPOINT
# -----------------------------
@app.post("/analyze-answer")
def analyze_answer(req: AnswerRequest):
    score = random.randint(60, 90)
    confidence = random.choice(["Low", "Medium", "High"])
    nervousness = detect_nervousness(req.answer)

    return {
        "score": score,
        "confidence": confidence,
        "nervousness": nervousness,
        "feedback": "Answer is structured. Improve clarity and confidence."
    }
