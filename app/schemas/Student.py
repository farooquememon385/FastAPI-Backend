from pydantic import BaseModel
from typing import List
from .Course import CourseResponse

class StudentBase(BaseModel):
    name: str

class StudentCreate(StudentBase):
    pass

class StudentResponse(StudentBase):
    id: int
    enrolled_courses: List['CourseResponse'] = []

    class Config:
        orm_mode = True