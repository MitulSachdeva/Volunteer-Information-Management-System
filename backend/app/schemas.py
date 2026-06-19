from pydantic import BaseModel

class VolunteerCreate(BaseModel):
    name: str
    email: str
    phone: str
    age: int
    skills: str
    availability: str
    address: str

class VolunteerResponse(VolunteerCreate):
    id: int
    status: str

    class Config:
        from_attributes = True