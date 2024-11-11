from pydantic import BaseModel
from typing import List, Optional
from .Department import DepartmentBase 
from .Course import CourseBase
from .Student import StudentBase

class TeacherPayLoad(BaseModel):
    name: str
    department_name: str

class EnrolledPayLoad(BaseModel):
    student_name: str
    course_title: str

class CourseTaughtPayLoad(BaseModel):
    course_title: str
    teacher_name: str
    department_name: str

class insertPayLoad(BaseModel):
   departments: Optional[List[DepartmentBase]] = []
   teachers: Optional[List[TeacherPayLoad]] = []
   courses: Optional[List[CourseBase]] = []
   students: Optional[List[StudentBase]] = []
   enrolleds: Optional[List[EnrolledPayLoad]] = []
   courseTaughts: Optional[List[CourseTaughtPayLoad]] = []
