from database import get_db
from sqlalchemy.orm import Session
from fastapi import Depends
from schemas.PayLoad import insertPayLoad
from models import Department, Teacher, Course, Student, Enrolled, CourseTaught
import crud

async def insert_data(payload: insertPayLoad, db: Session = Depends(get_db)):
    # Insert departments
    for dept in payload.departments:
        existing_department = crud.get_department_by_name(db, dept.name)
        if not existing_department:
            department = Department(name=dept.name)

    # Insert teachers
    for teacher in payload.teachers:
        existing_teacher = crud.get_teacher_by_name(db, teacher.name)
        if not existing_teacher:
            department = crud.get_department_by_name(db, teacher.department_name)
            if not department:
                department = Department(name=teacher.department_name)
            Teacher(name=teacher.name, department_id=department.id)

    # Insert courses
    for course in payload.courses:
        existing_course = crud.get_course_by_title(db, course.title)
        if not existing_course:
            Course(title=course.title)

    # Insert students and enrollments
    for student in payload.students:
        existing_student = crud.get_student_by_name(db, student.name)
        if not existing_student:
            Student(name=student.name)
        
    for enrolled in payload.enrolleds:
        course = crud.get_course_by_title(db, enrolled.course_title)
        if not course:
            course =Course(title=enrolled.course_title)
        student = crud.get_student_by_name(db, enrolled.student_name)
        if not student:
            student = Student(name=enrolled.student_name)
        existing_enrolled = crud.get_enrolled_by_student_and_course(db, student.id, course.id)
        if not existing_enrolled:
            Enrolled(student_id=student.id, course_id=course.id)
    
    for course_taught in payload.courseTaughts:
        teacher = crud.get_teacher_by_name(db, course_taught.teacher_name)
        if not teacher:
            department = crud.get_department_by_name(db, course_taught.department_name)
            if not department:
                department = Department(name=course_taught.department_name)
            teacher = Teacher(name=course_taught.teacher_name, department_id=department.id)
        if not course:
            course = Course(title=course_taught.course_title)
        existing_course_taught = crud.get_courseTaught_by_teacher_and_course(db, teacher.id, course.id)
        if not existing_course_taught:
            CourseTaught(teacher_id=teacher.id, course_id=course.id)

    return {"message": "Data inserted successfully"}

