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
