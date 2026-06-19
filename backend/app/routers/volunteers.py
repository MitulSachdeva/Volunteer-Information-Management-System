from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..database import SessionLocal
from ..models import Volunteer
from ..schemas import VolunteerCreate

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/volunteers")
def create_volunteer(
    volunteer: VolunteerCreate,
    db: Session = Depends(get_db)
):
    new_volunteer = Volunteer(**volunteer.dict())

    db.add(new_volunteer)
    db.commit()
    db.refresh(new_volunteer)

    return new_volunteer

@router.get("/volunteers")
def get_volunteers(
    db: Session = Depends(get_db)
):
    return db.query(Volunteer).all()

@router.delete("/volunteers/{volunteer_id}")
def delete_volunteer(
    volunteer_id: int,
    db: Session = Depends(get_db)
):
    volunteer = db.query(Volunteer).filter(
        Volunteer.id == volunteer_id
    ).first()

    if volunteer:
        db.delete(volunteer)
        db.commit()

    return {"message": "Deleted"}