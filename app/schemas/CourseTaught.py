from pydantic import BaseModel
from .Teacher import TeacherResponse
from .Course import CourseResponse 

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
