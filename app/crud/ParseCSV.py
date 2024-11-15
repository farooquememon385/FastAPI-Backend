from fastapi import UploadFile, File, HTTPException, Depends
from sqlalchemy.orm import Session
from database import get_db
import csv
from io import StringIO
from models import Department, Teacher, Course, Student, Enrolled, CourseTaught
import crud

async def parse_csv(file: UploadFile = File(...), db: Session = Depends(get_db)):
    if not file.filename.endswith('.csv'):
        raise HTTPException(status_code=400, detail="File format not supported. Please upload a CSV file.")
    content = await file.read()
    csv_reader = csv.DictReader(StringIO(content.decode("utf-8")))

    departments = []
    teachers = []
    courses = []
    students = []
    enrollments = []
    course_taught_records = []

    for row in csv_reader:
        # Example CSV format: ID, DepartmentName, TeacherName, CourseTitle, StudentName

        department_name = row.get("DepartmentName")
        teacher_name = row.get("TeacherName")
        course_title = row.get("CourseTitle")
        student_name = row.get("StudentName")

        if department_name:
            department = crud.get_department_by_name(db, department_name)  # Check if it exists
            if not department:
                department = Department(name=department_name)
                departments.append(department)

        if teacher_name and department_name:
            teacher = crud.get_teacher_by_name(db, teacher_name)
            if not teacher and department.id:
                teacher = Teacher(name=teacher_name, department_id=department.id)
                teachers.append(teacher)

        if course_title:
            course = crud.get_course_by_title(db, course_title)
            if not course:
                course = Course(title=course_title)
                courses.append(course)

        if student_name:
            student = crud.get_student_by_name(db, student_name)
            if not student:
                student = Student(name=student_name)
                students.append(student)

        if course_title and course.id and student_name and student.id:
            # Check if the student is already enrolled in the course
            existing_enrollment = db.query(Enrolled).filter_by(student_id=student.id, course_id=course.id).first()
            if not existing_enrollment and student and course:
                enrollment = Enrolled(student_id=student.id, course_id=course.id)
                enrollments.append(enrollment)

        if teacher_name  and teacher.id and course_title and course.id:
            # Check if the teacher is already teaching the course
            existing_course_taught = db.query(CourseTaught).filter_by(teacher_id=teacher.id, course_id=course.id).first()
            if not existing_course_taught:
                course_taught = CourseTaught(teacher_id=teacher.id, course_id=course.id)
                course_taught_records.append(course_taught)

    # Bulk insert collected data
    try:
        # Use bulk_save_objects to insert all at once for better performance
        db.bulk_save_objects(departments)
        db.bulk_save_objects(teachers)
        db.bulk_save_objects(courses)
        db.bulk_save_objects(students)
        db.bulk_save_objects(enrollments)
        db.bulk_save_objects(course_taught_records)
        db.commit()
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Failed to insert data: {str(e)}")

    return {"message": "CSV file processed and data inserted successfully"}
