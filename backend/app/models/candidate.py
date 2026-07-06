from sqlalchemy import Column, Integer, String, Float, Text

from app.database.base import Base


class Candidate(Base):
    __tablename__ = "candidates"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)

    email = Column(String, unique=True)

    phone = Column(String)

    skills = Column(Text)

    resume_text = Column(Text)

    score = Column(Float, default=0.0)