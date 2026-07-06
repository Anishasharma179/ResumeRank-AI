from app.services.resume_extractor import extract_skills


def calculate_match_score(
    resume_text: str,
    job_description: str
) -> float:
    """
    Calculates a skill match percentage between
    a resume and a job description.
    """

    resume_skills = set(extract_skills(resume_text))
    jd_skills = set(extract_skills(job_description))

    if not jd_skills:
        return 0.0

    matched_skills = resume_skills.intersection(jd_skills)

    score = (len(matched_skills) / len(jd_skills)) * 100

    return round(score, 2)