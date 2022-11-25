from .database import Base
from sqlalchemy import Column, Integer, String, DateTime, Float, Boolean, JSON
from sqlalchemy.sql import func


class Plan(Base):
    __tablename__ = "plan"

    id = Column(Integer(), primary_key=True)
    originalId = Column(String, unique=True, nullable=False)
    talentId = Column(String, nullable=True)
    talentName = Column(String, nullable=True)
    talentGrade = Column(String, nullable=True)
    bookingGrade = Column(String, nullable=True)
    operatingUnit = Column(String, nullable=False)
    officeCity = Column(String, nullable=True)
    officePostalCode = Column(String, nullable=False)
    jobManagerName = Column(String, nullable=True)
    jobManagerId = Column(String, nullable=True)
    totalHours = Column(Float(), nullable=False)
    startDate = Column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    endDate = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    clientName = Column(String, nullable=True)
    clientId = Column(String, nullable=False)
    industry = Column(String, nullable=True)
    isUnassigned = Column(Boolean(), nullable=True)
    requiredSkills = Column(JSON, nullable=True)
    optionalSkills = Column(JSON, nullable=True)

    def __repr__(self) -> str:
        return f"ID: {self.id}"
