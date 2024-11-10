from pydantic import BaseModel
from typing import List
from .Teacher import TeacherResponse

class DepartmentBase(BaseModel):
    name: str

class DepartmentCreate(DepartmentBase):
    pass

class DepartmentResponse(DepartmentBase):
    id: int
    teachers: List['TeacherResponse'] = []

    class Config:
        orm_mode = True