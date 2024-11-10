from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
import crud
from database import get_db
import schemas
import schemas.Enrolled
import crud

enrolled_router = APIRouter(
    prefix="/enrolleds",
    tags=["enrolleds"]
)

@enrolled_router.get("/", response_model=List[schemas.Enrolled.EnrolledResponse])
def get_enrolleds(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    enrolleds = crud.get_enrolleds(db, skip=skip, limit=limit)
    return enrolleds

@enrolled_router.get("/{enrolled_id}", response_model=schemas.Enrolled.EnrolledResponse)
def get_enrolled(enrolled_id: int, db: Session = Depends(get_db)):
    enrolled = crud.get_enrolled(db, enrolled_id)
    if enrolled is None:
        raise HTTPException(status_code=404, detail="Enrolled not found")
    return enrolled

@enrolled_router.post("/", response_model=schemas.Enrolled.EnrolledResponse)
def create_enrolled(enrolled: schemas.Enrolled.EnrolledCreate, db: Session = Depends(get_db)):
    db_course = crud.get_course(db, enrolled.course_id)
    if db_course is None:
        raise HTTPException(status_code=404, detail="Department not found")
    db_student = crud.get_student(db, enrolled.student_id)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return crud.create_enrolled(db, enrolled)

@enrolled_router.delete("/{enrolled_id}", response_model=schemas.Enrolled.EnrolledResponse)
def delete_enrolled(enrolled_id: int, db: Session = Depends(get_db)):
    deleted_enrolled = crud.delete_enrolled(db, enrolled_id)
    if deleted_enrolled is None:
        raise HTTPException(status_code=404, detail="Enrolled not found")
    return deleted_enrolled