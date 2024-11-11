from database import get_db
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException
from schemas.PayLoad import insertPayLoad
import crud

def insert_data(payload: insertPayLoad, db: Session = Depends(get_db)):
    # Insert departments
    print(payload)
    for dept in payload.departments:
        existing_department = crud.get_department_by_name(db, dept.name)
        if not existing_department:
            crud.create_department(db, name=dept.name)

    # Insert teachers
    for teacher in payload.teachers:
        existing_teacher = crud.get_teacher_by_name(db, teacher.name)
        if not existing_teacher:
            department = crud.get_department_by_name(db, teacher.department_name)
            if not department:
                department = crud.create_department(db, name=teacher.department_name)
            crud.create_teacher(db, name=teacher.name, department_id=department.id)

    # Insert courses
    for course in payload.courses:
        existing_course = crud.get_course_by_title(db, course.title)
        if not existing_course:
            crud.create_course(db, title=course.title)

    # Insert students and enrollments
    for student in payload.students:
        existing_student = crud.get_student_by_name(db, student.name)
        if not existing_student:
            crud.create_student(db, name=student.name)
        
    for enrolled in payload.enrolleds:
        course = crud.get_course_by_title(db, enrolled.course_title)
        if not course:
            course = crud.create_course(db, title=enrolled.course_title)
        student = crud.get_student_by_name(db, enrolled.student_name)
        if not student:
            student = crud.create_student(db, name=enrolled.student_name)
        existing_enrolled = crud.get_enrolled_by_student_and_course(db, student.id, course.id)
        if not existing_enrolled:
            crud.create_enrolled(db, student_id=student.id, course_id=course.id)
    
    for course_taught in payload.courseTaughts:
        teacher = crud.get_teacher_by_name(db, course_taught.teacher_name)
        if not teacher:
            department = crud.get_department_by_name(db, course_taught.department_name)
            if not department:
                department = crud.create_department(db, name=course_taught.department_name)
            teacher = crud.create_teacher(db, name=course_taught.teacher_name, department_id=department.id)
        if not course:
            course = crud.create_course(db, title=course_taught.course_title)
        existing_course_taught = crud.get_courseTaught(db, teacher.id, course.id)
        if not existing_course_taught:
            crud.create_courseTaught(db, teacher_id=teacher.id, course_id=course.id)

    return {"message": "Data inserted successfully"}

