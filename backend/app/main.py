from fastapi import FastAPI

from app.database.session import engine
from app.database.base import Base

from app.api.upload import router as upload_router
from app.api.job import router as job_router

import app.models.candidate

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="ResumeRank AI",
    description="AI-Powered Resume Screening & Candidate Ranking System",
    version="1.0.0"
)

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