from pydantic import BaseModel

class CourseBase(BaseModel):
    title: str

class CourseCreate(CourseBase):
    pass

class CourseResponse(CourseBase):
    id: int

    class Config:
        orm_mode = True