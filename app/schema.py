# pylint: disable=no-name-in-module
from pydantic import BaseModel, Field
from datetime import datetime


# response model sechema
class planner(BaseModel):
    id: int = Field(default=None, description="unique ID")
    originalId: str = Field(default=None, description="original ID")
    talentId: str = Field(default=None, description="talent ID")
    talentName: str = Field(default=None, description="Talent name")
    talentGrade: str = Field(default=None, description="Grade of talent")
    bookingGrade: str = Field(default=None, description="Booking Grade")
    operatingUnit: str = Field(default=None, description="Operating Unit")
    officeCity: str = Field(default=None, description="Office city")
    officePostalCode: str = Field(default=None, description="office postal code")
    jobManagerName: str = Field(default=None, description="Name of Job manager")
    jobManagerId: str = Field(default=None, description="Job Manager ID")
    totalHours: float = Field(default=None, description="total Hours spent")
    startDate: datetime = Field(default=None, description="starting Date")
    endDate: datetime = Field(default=None, description="Ending Date")
    clientName: str = Field(default=None, description="Name of Client")
    clientId: str = Field(default=None, description="Client ID")
    industry: str = Field(default=None, description="Industry")
    isUnassigned: bool = Field(default=None, description="Is assigned (True/False)")
    requiredSkills: object = Field(default=None, description="Required Skills")
    optionalSkills: object = Field(default=None, description="Optional Skills")

    class Config:
        orm_mode = True
