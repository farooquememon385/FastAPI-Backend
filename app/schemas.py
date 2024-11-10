from pydantic import BaseModel
from typing import List

# Department Schemas
class DepartmentBase(BaseModel):
    name: str

class DepartmentCreate(DepartmentBase):
    pass

class DepartmentResponse(DepartmentBase):
    id: int
    teachers: List['TeacherResponse'] = []

    class Config:
        orm_mode = True

# Teacher Schemas
class TeacherBase(BaseModel):
    name: str
    department_id: int

class TeacherCreate(TeacherBase):
    pass

class TeacherResponse(TeacherBase):
    id: int
    courses: List['CourseResponse'] = []
    department: DepartmentResponse

    class Config:
        orm_mode = True

# Course Schemas
class CourseBase(BaseModel):
    title: str

class CourseCreate(CourseBase):
    pass

class CourseResponse(CourseBase):
    id: int
    teachers: List['TeacherResponse'] = []
    students: List['StudentResponse'] = []

    class Config:
        orm_mode = True

# Student Schemas
class StudentBase(BaseModel):
    name: str

class StudentCreate(StudentBase):
    pass

class StudentResponse(StudentBase):
    id: int
    enrolled_courses: List['CourseResponse'] = []

    class Config:
        orm_mode = True

# Enrolled Schemas (for Many-to-Many between Student and Course)
class EnrolledBase(BaseModel):
    student_id: int
    course_id: int

class EnrolledCreate(EnrolledBase):
    pass

class EnrolledResponse(EnrolledBase):
    id: int
    student: StudentResponse
    course: CourseResponse

    class Config:
        orm_mode = True

# CourseTaught Schemas (for Many-to-Many between Teacher and Course)
class CourseTaughtBase(BaseModel):
    teacher_id: int
    course_id: int

class CourseTaughtCreate(CourseTaughtBase):
    pass

class CourseTaughtResponse(CourseTaughtBase):
    id: int
    teacher: TeacherResponse
    course: CourseResponse

    class Config:
        orm_mode = True
