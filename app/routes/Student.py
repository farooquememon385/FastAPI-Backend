from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
import crud.Student
from database import get_db
import schemas
import schemas.Student
import crud

student_router = APIRouter(
    prefix="/students",
    tags=["students"]
)

@student_router.get("/", response_model=List[schemas.Student.StudentResponse])
def get_students(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    students = crud.get_students(db, skip=skip, limit=limit)
    return students

@student_router.get("/{student_id}", response_model=schemas.Student.StudentResponse)
def get_student(student_id: int, db: Session = Depends(get_db)):
    student = crud.get_student(db, student_id)
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@student_router.post("/", response_model=schemas.Student.StudentResponse)
def create_student(student: schemas.Student.StudentCreate, db: Session = Depends(get_db)):
    return crud.create_student(db, student)

@student_router.put("/{student_id}", response_model=schemas.Student.StudentResponse)
def update_student(student_id: int, student: schemas.Student.StudentCreate, db: Session = Depends(get_db)):
    updated_student = crud.update_student(db, student_id, student)
    if updated_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return updated_student

@student_router.delete("/{student_id}", response_model=schemas.Student.StudentResponse)
def delete_student(student_id: int, db: Session = Depends(get_db)):
    deleted_student = crud.delete_student(db, student_id)
    if deleted_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return deleted_student