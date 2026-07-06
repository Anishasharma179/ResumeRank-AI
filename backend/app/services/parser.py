import pdfplumber
from docx import Document


def extract_text_from_docx(file_path: str) -> str:
    document = Document(file_path)

    return "\n".join(
        paragraph.text
        for paragraph in document.paragraphs
    )
from pathlib import Path


def extract_text_from_pdf(file_path: str) -> str:
    text = ""

    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    return text
def extract_text(file_path: str) -> str:
    extension = Path(file_path).suffix.lower()

    if extension == ".pdf":
        return extract_text_from_pdf(file_path)

    if extension == ".docx":
        return extract_text_from_docx(file_path)

    raise ValueError("Unsupported file type")