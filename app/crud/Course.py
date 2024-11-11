from sqlalchemy.orm import Session
from models import Course
from schemas.Course import CourseCreate

def get_course(db: Session, course_id: int):
    return db.query(Course).filter(Course.id == course_id).first()

def get_course_by_title(db: Session, title: str):
    return db.query(Course).filter(Course.title == title).first()

def get_courses(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Course).offset(skip).limit(limit).all()

def create_course(db: Session, course: CourseCreate):
    db_course = Course(title=course.title)
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course


def update_course(db: Session, course_id: int, course: CourseCreate):
    db_course = get_course(db, course_id)
    if db_course:
        db_course.title = course.title
        db.commit()
        db.refresh(db_course)
        return db_course
    return None

def delete_course(db: Session, course_id: int):
    db_course = get_course(db, course_id)
    if db_course:
        db.delete(db_course)
        db.commit()
        return db_course
    return None
