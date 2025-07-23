from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from . import crud, schemas
from .database import SessionLocal

router = APIRouter()

async def get_db():
    async with SessionLocal() as session:
        yield session

@router.post("/students/", response_model=schemas.Student)
async def create_student(student: schemas.StudentCreate, db: AsyncSession = Depends(get_db)):
    return await crud.create_student(db, student)

@router.get("/students/", response_model=list[schemas.Student])
async def read_students(db: AsyncSession = Depends(get_db)):
    return await crud.get_students(db)

@router.post("/grades/", response_model=schemas.Grade)
async def create_student(grade: schemas.GradeCreate, db: AsyncSession = Depends(get_db)):
    return await crud.create_grade(db, grade)

@router.get("/grades/", response_model=list[schemas.Grade])
async def read_students(db: AsyncSession = Depends(get_db)):
    return await crud.get_grades(db)

@router.post("/subjects/", response_model=schemas.Subject)
async def create_subject(subject: schemas.SubjectCreate, db: AsyncSession = Depends(get_db)):
    return await crud.create_subject(db, subject)

@router.get("/subjects/", response_model=list[schemas.Subject])
async def read_subjects(db: AsyncSession = Depends(get_db)):
    return await crud.get_subjects(db)


