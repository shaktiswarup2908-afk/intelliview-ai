
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from auth import router as auth_router
from interview import router as interview_router

app = FastAPI(title="IntelliView AI")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(auth_router)
app.include_router(interview_router)

@app.get("/")
def root():
    return {"status": "IntelliView Backend Running"}
