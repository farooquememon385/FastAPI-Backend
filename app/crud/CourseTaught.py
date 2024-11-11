from sqlalchemy.orm import Session
from models import CourseTaught
from schemas.CourseTaught import CourseTaughtCreate

def get_courseTaught(db: Session, courseTaught_id: int):
    return db.query(CourseTaught).filter(CourseTaught.id == courseTaught_id).first()

def get_courseTaught_by_teacher_and_course(db: Session, teacher_id: int, course_id: int):
    return db.query(CourseTaught).filter(CourseTaught.teacher_id == teacher_id, CourseTaught.course_id == course_id).first()

def get_courseTaughts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(CourseTaught).offset(skip).limit(limit).all()

def create_courseTaught(db: Session, courseTaught: CourseTaughtCreate):
    db_courseTaught = CourseTaught(teacher_id=courseTaught.teacher_id, course_id=courseTaught.course_id)
    db.add(db_courseTaught)
    db.commit()
    db.refresh(db_courseTaught)
    return db_courseTaught


def delete_courseTaught(db: Session, courseTaught_id: int):
    db_courseTaught = get_courseTaught(db, courseTaught_id)
    if db_courseTaught:
        db.delete(db_courseTaught)
        db.commit()
        return db_courseTaught
    return None
