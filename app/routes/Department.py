from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
import crud.Department
from database import get_db
import schemas
import schemas.Department
import crud

department_router = APIRouter(
    prefix="/departments",
    tags=["departments"]
)

@department_router.get("/", response_model=List[schemas.Department.DepartmentResponse])
def get_departments(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    departments = crud.get_departments(db, skip=skip, limit=limit)
    return departments

@department_router.get("/{department_id}", response_model=schemas.Department.DepartmentResponse)
def get_department(department_id: int, db: Session = Depends(get_db)):
    department = crud.get_department(db, department_id)
    if department is None:
        raise HTTPException(status_code=404, detail="Department not found")
    return department

@department_router.post("/", response_model=schemas.Department.DepartmentResponse)
def create_department(department: schemas.Department.DepartmentCreate, db: Session = Depends(get_db)):
    return crud.create_department(db, department)

@department_router.put("/{department_id}", response_model=schemas.Department.DepartmentResponse)
def update_department(department_id: int, department: schemas.Department.DepartmentCreate, db: Session = Depends(get_db)):
    updated_department = crud.update_department(db, department_id, department)
    if updated_department is None:
        raise HTTPException(status_code=404, detail="Department not found")
    return updated_department

@department_router.delete("/{department_id}", response_model=schemas.Department.DepartmentResponse)
def delete_department(department_id: int, db: Session = Depends(get_db)):
    deleted_department = crud.delete_department(db, department_id)
    if deleted_department is None:
        raise HTTPException(status_code=404, detail="Department not found")
    return deleted_department