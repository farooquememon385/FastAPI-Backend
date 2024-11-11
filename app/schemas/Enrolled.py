from pydantic import BaseModel
from .Student import StudentResponse
from .Course import CourseResponse

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
