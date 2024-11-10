from sqlalchemy.orm import Session
from models import Student
from schemas.Student import StudentCreate

def get_student(db: Session, student_id: int):
    return db.query(Student).filter(Student.id == student_id).first()

def get_students(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Student).offset(skip).limit(limit).all()

def create_student(db: Session, student: StudentCreate):
    db_student = Student(name=student.name)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student


def update_student(db: Session, student_id: int, student: StudentCreate):
    db_student = get_student(db, student_id)
    if db_student:
        db_student.name = student.name
        db.commit()
        db.refresh(db_student)
        return db_student
    return None

def delete_student(db: Session, student_id: int):
    db_student = get_student(db, student_id)
    if db_student:
        db.delete(db_student)
        db.commit()
        return db_student
    return None
