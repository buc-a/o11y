from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from . import models, schemas

async def create_student(db: AsyncSession, student: schemas.StudentCreate):
    db_student = models.Student(**student.dict())
    db.add(db_student)
    await db.commit()
    await db.refresh(db_student)
    return db_student

async def get_students(db: AsyncSession):
    result = await db.execute(select(models.Student))
    return result.scalars().all()

async def create_subject(db: AsyncSession, subject: schemas.SubjectCreate):
    db_subject = models.Subject(**subject.dict())
    db.add(db_subject)
    await db.commit()
    await db.refresh(db_subject)
    return db_subject


async def get_subjects(db: AsyncSession):
    result = await db.execute(select(models.Subject))
    return result.scalars().all()

async def create_grade(db: AsyncSession, grade: schemas.GradeCreate):
    db_grade = models.Grade(**grade.dict())
    db.add(db_grade)
    await db.commit()
    await db.refresh(db_grade)
    return db_grade

async def get_grades(db: AsyncSession):
    result = await db.execute(select(models.Grade))
    return result.scalars().all()


