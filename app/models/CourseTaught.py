from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
from database import Base

class CourseTaught(Base):
    __tablename__ = 'course_taught'

    id = Column(Integer, primary_key=True, autoincrement=True)
    teacher_id = Column(Integer, ForeignKey('teacher.id'), nullable=False)
    course_id = Column(Integer, ForeignKey('course.id'), nullable=False)
    teacher = relationship('Teacher', back_populates='courses')
    course = relationship('Course', back_populates='teachers')

