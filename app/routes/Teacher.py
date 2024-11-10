from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
import crud.Teacher
import crud.Department
from database import get_db
import schemas
import schemas.Teacher
import crud

teacher_router = APIRouter(
    prefix="/teachers",
    tags=["teachers"]
)

@teacher_router.get("/", response_model=List[schemas.Teacher.TeacherResponse])
def get_teachers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    teachers = crud.get_teachers(db, skip=skip, limit=limit)
    return teachers

@teacher_router.get("/{teacher_id}", response_model=schemas.Teacher.TeacherResponse)
def get_teacher(teacher_id: int, db: Session = Depends(get_db)):
    teacher = crud.get_teacher(db, teacher_id)
    if teacher is None:
        raise HTTPException(status_code=404, detail="Teacher not found")
    return teacher

@teacher_router.post("/", response_model=schemas.Teacher.TeacherResponse)
def create_teacher(teacher: schemas.Teacher.TeacherCreate, db: Session = Depends(get_db)):
    db_department = crud.get_department(db, teacher.department_id)
    if db_department is None:
        raise HTTPException(status_code=404, detail="Department not found")
    return crud.create_teacher(db, teacher)

@teacher_router.put("/{teacher_id}", response_model=schemas.Teacher.TeacherResponse)
def update_teacher(teacher_id: int, teacher: schemas.Teacher.TeacherCreate, db: Session = Depends(get_db)):
    db_department = crud.get_department(db, teacher.department_id)
    if db_department is None:
        raise HTTPException(status_code=404, detail="Department not found")
    updated_teacher = crud.update_teacher(db, teacher_id, teacher)
    if updated_teacher is None:
        raise HTTPException(status_code=404, detail="Teacher not found")
    return updated_teacher

@teacher_router.delete("/{teacher_id}", response_model=schemas.Teacher.TeacherResponse)
def delete_teacher(teacher_id: int, db: Session = Depends(get_db)):
    deleted_teacher = crud.delete_teacher(db, teacher_id)
    if deleted_teacher is None:
        raise HTTPException(status_code=404, detail="Teacher not found")
    return deleted_teacher