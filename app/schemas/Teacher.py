from typing import List
from pydantic import BaseModel
from .Department import DepartmentResponse
from .Course import CourseResponse

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
