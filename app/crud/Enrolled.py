from sqlalchemy.orm import Session
from models import Enrolled
from schemas.Enrolled import EnrolledCreate

def get_enrolled(db: Session, enrolled_id: int):
    return db.query(Enrolled).filter(Enrolled.id == enrolled_id).first()

def get_enrolleds(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Enrolled).offset(skip).limit(limit).all()

def create_enrolled(db: Session, enrolled: EnrolledCreate):
    db_enrolled = Enrolled(student_id=enrolled.student_id, course_id=enrolled.course_id)
    db.add(db_enrolled)
    db.commit()
    db.refresh(db_enrolled)
    return db_enrolled


def delete_enrolled(db: Session, enrolled_id: int):
    db_enrolled = get_enrolled(db, enrolled_id)
    if db_enrolled:
        db.delete(db_enrolled)
        db.commit()
        return db_enrolled
    return None
