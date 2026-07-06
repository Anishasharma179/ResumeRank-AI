import re
import phonenumbers
import spacy

nlp = spacy.load("en_core_web_sm")


def extract_name(text: str) -> str:
    doc = nlp(text)

    for entity in doc.ents:
        if entity.label_ == "PERSON":
            return entity.text

    return ""


def extract_email(text: str) -> str:
    pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"

    match = re.search(pattern, text)

    if match:
        return match.group()

    return ""

def extract_phone(text: str) -> str:
    try:
        for match in phonenumbers.PhoneNumberMatcher(text, "IN"):
            return phonenumbers.format_number(
                match.number,
                phonenumbers.PhoneNumberFormat.E164
            )
    except Exception:
        pass

    return ""

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
    "html",
    "css",
    "javascript",
    "react"
}

def extract_skills(text: str) -> list[str]:
    text = text.lower()

    found_skills = []

    for skill in SKILLS:
        if skill in text:
            found_skills.append(skill.title())

    return sorted(found_skills)

def extract_resume_data(text: str) -> dict:
    return {
        "name": extract_name(text),
        "email": extract_email(text),
        "phone": extract_phone(text),
        "skills": extract_skills(text)
    }