from pathlib import Path
import shutil

from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.models.candidate import Candidate

from app.services.parser import extract_text
from app.services.ranker import calculate_match_score

router = APIRouter()

JOB_DIR = Path("job_descriptions")
JOB_DIR.mkdir(exist_ok=True)


@router.post("/job")
async def upload_job_description(
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

    destination = JOB_DIR / file.filename

    with destination.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    job_description = extract_text(str(destination))

    candidates = db.query(Candidate).all()

    ranked_candidates = []

    for candidate in candidates:
        score = calculate_match_score(
            candidate.resume_text,
            job_description
        )

        candidate.score = score

        ranked_candidates.append({
            "id": candidate.id,
            "name": candidate.name,
            "email": candidate.email,
            "phone": candidate.phone,
            "skills": candidate.skills,
            "score": score
        })

    db.commit()

    ranked_candidates.sort(
        key=lambda candidate: candidate["score"],
        reverse=True
    )

    return {
        "job_description": file.filename,
        "total_candidates": len(ranked_candidates),
        "rankings": ranked_candidates
    }