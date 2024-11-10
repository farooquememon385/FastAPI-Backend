from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
import crud.Course
from database import get_db
import schemas
import schemas.Course
import crud

course_router = APIRouter(
    prefix="/courses",
    tags=["courses"]
)

@course_router.get("/", response_model=List[schemas.Course.CourseResponse])
def get_courses(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    courses = crud.get_courses(db, skip=skip, limit=limit)
    return courses

@course_router.get("/{course_id}", response_model=schemas.Course.CourseResponse)
def get_course(course_id: int, db: Session = Depends(get_db)):
    course = crud.get_course(db, course_id)
    if course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    return course

@course_router.post("/", response_model=schemas.Course.CourseResponse)
def create_course(course: schemas.Course.CourseCreate, db: Session = Depends(get_db)):
    return crud.create_course(db, course)

@course_router.put("/{course_id}", response_model=schemas.Course.CourseResponse)
def update_course(course_id: int, course: schemas.Course.CourseCreate, db: Session = Depends(get_db)):
    updated_course = crud.update_course(db, course_id, course)
    if updated_course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    return updated_course

@course_router.delete("/{course_id}", response_model=schemas.Course.CourseResponse)
def delete_course(course_id: int, db: Session = Depends(get_db)):
    deleted_course = crud.delete_course(db, course_id)
    if deleted_course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    return deleted_course