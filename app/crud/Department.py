from sqlalchemy.orm import Session
from models import Department
from schemas.Department import DepartmentCreate

def get_department(db: Session, department_id: int):
    return db.query(Department).filter(Department.id == department_id).first()

def get_departments(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Department).offset(skip).limit(limit).all()

def create_department(db: Session, department: DepartmentCreate):
    db_department = Department(name=department.name)
    db.add(db_department)
    db.commit()
    db.refresh(db_department)
    return db_department


def update_department(db: Session, department_id: int, department: DepartmentCreate):
    db_department = get_department(db, department_id)
    if db_department:
        db_department.name = department.name
        db.commit()
        db.refresh(db_department)
        return db_department
    return None

def delete_department(db: Session, department_id: int):
    db_department = get_department(db, department_id)
    if db_department:
        db.delete(db_department)
        db.commit()
        return db_department
    return None
