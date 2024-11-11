from sqlalchemy.orm import Session
from models import Teacher
from schemas.Teacher import TeacherCreate

def get_teacher(db: Session, teacher_id: int):
    return db.query(Teacher).filter(Teacher.id == teacher_id).first()

def get_teacher_by_name(db: Session, teacher_name: str):
    return db.query(Teacher).filter(Teacher.name == teacher_name).first()

def get_teachers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Teacher).offset(skip).limit(limit).all()

def create_teacher(db: Session, teacher: TeacherCreate):
    db_teacher = Teacher(name=teacher.name, department_id=teacher.department_id)
    db.add(db_teacher)
    db.commit()
    db.refresh(db_teacher)
    return db_teacher


def update_teacher(db: Session, teacher_id: int, teacher: TeacherCreate):
    db_teacher = get_teacher(db, teacher_id)
    if db_teacher:
        db_teacher.name = teacher.name
        db_teacher.department_id = teacher.department_id
        db.commit()
        db.refresh(db_teacher)
        return db_teacher
    return None

def delete_teacher(db: Session, teacher_id: int):
    db_teacher = get_teacher(db, teacher_id)
    if db_teacher:
        db.delete(db_teacher)
        db.commit()
        return db_teacher
    return None
