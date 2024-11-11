from database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Enrolled(Base):
    __tablename__ = 'enrolled'

    id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(Integer, ForeignKey('student.id'), nullable=False)
    course_id = Column(Integer, ForeignKey('course.id'), nullable=False)
    student = relationship('Student', back_populates='enrolled_courses')
    course = relationship('Course', back_populates='students')
