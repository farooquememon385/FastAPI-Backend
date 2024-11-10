from database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Course(Base):
    __tablename__ = 'course'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    students = relationship('Enrolled', back_populates='course')
    teachers = relationship('CourseTaught', back_populates='course')
