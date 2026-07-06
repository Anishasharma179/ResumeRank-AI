import re


SKILLS = {
    "python",
    "java",
    "c",
    "c++",
    "sql",
    "mysql",
    "mongodb",
    "fastapi",
    "flask",
    "django",
    "machine learning",
    "deep learning",
    "tensorflow",
    "pytorch",
    "scikit-learn",
    "pandas",
    "numpy",
    "opencv",
    "git",
    "docker",
    "linux",
    "html",
    "css",
    "javascript",
    "react"
}


def extract_skills(text: str):
    text = text.lower()

    found = set()

    for skill in SKILLS:
        if re.search(rf"\b{re.escape(skill)}\b", text):
            found.add(skill)

    return found


def calculate_match_score(resume_text: str, job_text: str):
    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job_text)

    if not job_skills:
        return {
            "score": 0,
            "matched_skills": [],
            "missing_skills": []
        }

    matched = resume_skills.intersection(job_skills)
    missing = job_skills.difference(resume_skills)

    score = round(len(matched) / len(job_skills) * 100, 2)

    return {
        "score": score,
        "matched_skills": sorted(list(matched)),
        "missing_skills": sorted(list(missing))
    }