from pydantic import BaseModel
from typing import List
from .Teacher import TeacherResponse
from .Student import StudentResponse

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