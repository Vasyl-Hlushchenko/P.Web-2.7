from datetime import datetime

from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import DateTime


Base = declarative_base()


class Group(Base):
    __tablename__ = "groups"
    id = Column(Integer, primary_key=True)
    group_name = Column(String(150), nullable=False)


class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    full_name = Column(String(150), nullable=False)
    group_id = Column(Integer, ForeignKey(Group.id, ondelete="CASCADE"))

    groups = relationship("Group", backref="student")


class Teacher(Base):
    __tablename__ = "teachers"
    id = Column(Integer, primary_key=True)
    full_name = Column(String(50), nullable=False)

    subjects = relationship("Subject", backref="teacher")


class Subject(Base):
    __tablename__ = "subjects"
    id = Column(Integer, primary_key=True)
    subject_name = Column(String(50), nullable=False)
    teacher_id = Column(Integer, ForeignKey(Teacher.id, ondelete="CASCADE"))

    marks = relationship("Mark", backref="subject")


class Mark(Base):
    __tablename__ = "marks"
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey(Student.id, ondelete="CASCADE"))
    subject_id = Column(Integer, ForeignKey(Subject.id, ondelete="CASCADE"))
    mark = Column(Integer)
    date = Column(DateTime)

    students = relationship("Student", backref="mark")
