from pathlib import Path
import shutil

from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.models.candidate import Candidate

from app.services.parser import extract_text
from app.services.resume_extractor import extract_resume_data

print("=== NEW upload.py LOADED ===")

router = APIRouter()

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)


@router.post("/upload")
async def upload_resume(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    allowed_extensions = {".pdf", ".docx"}

    extension = Path(file.filename).suffix.lower()

    if extension not in allowed_extensions:
        raise HTTPException(
            status_code=400,
            detail="Only PDF and DOCX files are allowed."
        )

    destination = UPLOAD_DIR / file.filename

    with destination.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    try:
        resume_text = extract_text(str(destination))
        candidate_data = extract_resume_data(resume_text)
    except Exception as e:
        print("ERROR:", repr(e))
        raise

    # Check if candidate already exists
    existing_candidate = (
        db.query(Candidate)
        .filter(Candidate.email == candidate_data["email"])
        .first()
    )

    if existing_candidate:
        # Update existing candidate
        existing_candidate.name = candidate_data["name"] or "Unknown"
        existing_candidate.phone = candidate_data["phone"]
        existing_candidate.skills = ", ".join(candidate_data["skills"])
        existing_candidate.resume_text = resume_text

        db.commit()
        db.refresh(existing_candidate)

    else:
        # Insert new candidate
        candidate = Candidate(
            name=candidate_data["name"] or "Unknown",
            email=candidate_data["email"],
            phone=candidate_data["phone"],
            skills=", ".join(candidate_data["skills"]),
            resume_text=resume_text,
            score=0.0
        )

        db.add(candidate)
        db.commit()
        db.refresh(candidate)

    return {
    "filename": file.filename,
    "status": "uploaded successfully",
    "candidate": candidate_data,
    "resume_text": resume_text
}


@router.get("/candidates")
def get_candidates(db: Session = Depends(get_db)):
    candidates = db.query(Candidate).all()
    return candidates