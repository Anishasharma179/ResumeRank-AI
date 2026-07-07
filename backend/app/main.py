from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database.session import engine
from app.database.base import Base

from app.api.upload import router as upload_router
from app.api.job import router as job_router

import app.models.candidate

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="ResumeRank AI",
    description="AI-Powered Resume Screening & Candidate Ranking System",
    version="1.0.0",
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
    "http://localhost:5173",
    "http://localhost:5174",
    "http://localhost:5175",
    "http://127.0.0.1:5173",
    "http://127.0.0.1:5174",
    "http://127.0.0.1:5175",
    "https://resume-rank-ai-one.vercel.app",
],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(upload_router, prefix="/api", tags=["Resume Upload"])
app.include_router(job_router, prefix="/api", tags=["Job Description"])


@app.get("/")
def root():
    return {
        "message": "Welcome to ResumeRank AI 🚀"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }