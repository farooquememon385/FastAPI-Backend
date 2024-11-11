from pydantic import BaseModel
from .Department import DepartmentResponse

class TeacherBase(BaseModel):
    name: str
    department_id: int

class TeacherCreate(TeacherBase):
    pass

class TeacherResponse(TeacherBase):
    id: int
    department: DepartmentResponse

    class Config:
        orm_mode = True
