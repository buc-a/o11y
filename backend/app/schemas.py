from pydantic import BaseModel
from typing import List

class StudentBase(BaseModel):
    name: str

class StudentCreate(StudentBase):
    pass

class Student(StudentBase):
    id: int
    class Config:
        orm_mode = True

class SubjectBase(BaseModel):
    title: str

class SubjectCreate(SubjectBase):
    pass

class Subject(SubjectBase):
    id: int
    class Config:
        orm_mode = True

class GradeBase(BaseModel):
    value: float
    student_id: int
    subject_id: int

class GradeCreate(GradeBase):
    pass

class Grade(GradeBase):
    id: int
    class Config:
        orm_mode = True

