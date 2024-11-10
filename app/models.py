from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base


Base = declarative_base()

class Department(Base):
    __tablename__ = 'department'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    teachers = relationship('Teacher', back_populates='department')

class Teacher(Base):
    __tablename__ = 'teacher'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    department_id = Column(Integer, ForeignKey('department.id'))
    department = relationship('Department', back_populates='teachers')
    courses = relationship('CourseTaught', back_populates='teacher')

class Course(Base):
    __tablename__ = 'course'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    students = relationship('Enrolled', back_populates='course')
    teachers = relationship('CourseTaught', back_populates='course')

class Student(Base):
    __tablename__ = 'student'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    enrolled_courses = relationship('Enrolled', back_populates='student')

class Enrolled(Base):
    __tablename__ = 'enrolled'

    id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(Integer, ForeignKey('student.id'), nullable=False)
    course_id = Column(Integer, ForeignKey('course.id'), nullable=False)
    student = relationship('Student', back_populates='enrolled_courses')
    course = relationship('Course', back_populates='students')

class CourseTaught(Base):
    __tablename__ = 'course_taught'

    id = Column(Integer, primary_key=True, autoincrement=True)
    teacher_id = Column(Integer, ForeignKey('teacher.id'), nullable=False)
    course_id = Column(Integer, ForeignKey('course.id'), nullable=False)
    teacher = relationship('Teacher', back_populates='courses')
    course = relationship('Course', back_populates='teachers')

