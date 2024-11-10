from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
import crud
from database import get_db
import schemas
import schemas.CourseTaught
import crud

courseTaught_router = APIRouter(
    prefix="/courseTaughts",
    tags=["courseTaughts"]
)

@courseTaught_router.get("/", response_model=List[schemas.CourseTaught.CourseTaughtResponse])
def get_courseTaughts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    courseTaughts = crud.get_courseTaughts(db, skip=skip, limit=limit)
    return courseTaughts

@courseTaught_router.get("/{courseTaught_id}", response_model=schemas.CourseTaught.CourseTaughtResponse)
def get_courseTaught(courseTaught_id: int, db: Session = Depends(get_db)):
    courseTaught = crud.get_courseTaught(db, courseTaught_id)
    if courseTaught is None:
        raise HTTPException(status_code=404, detail="CourseTaught not found")
    return courseTaught

@courseTaught_router.post("/", response_model=schemas.CourseTaught.CourseTaughtResponse)
def create_courseTaught(courseTaught: schemas.CourseTaught.CourseTaughtCreate, db: Session = Depends(get_db)):
    db_course = crud.get_course(db, courseTaught.course_id)
    if db_course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    db_teacher = crud.get_teacher(db, courseTaught.teacher_id)
    if db_teacher is None:
        raise HTTPException(status_code=404, detail="Teacher not found")
    return crud.create_courseTaught(db, courseTaught)

@courseTaught_router.delete("/{courseTaught_id}", response_model=schemas.CourseTaught.CourseTaughtResponse)
def delete_courseTaught(courseTaught_id: int, db: Session = Depends(get_db)):
    deleted_courseTaught = crud.delete_courseTaught(db, courseTaught_id)
    if deleted_courseTaught is None:
        raise HTTPException(status_code=404, detail="CourseTaught not found")
    return deleted_courseTaught