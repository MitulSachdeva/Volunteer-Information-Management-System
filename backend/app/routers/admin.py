from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..database import SessionLocal
from ..models import Volunteer

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/admin/stats")
def stats(
    db: Session = Depends(get_db)
):
    volunteers = db.query(
        Volunteer
    ).all()

    return {
        "total_volunteers":
            len(volunteers),

        "active_volunteers":
            len([
                v for v in volunteers
                if v.status == "Active"
            ])
    }