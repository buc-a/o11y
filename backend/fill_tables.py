import asyncio
from app.database import SessionLocal
from app import models
from app.database import engine
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text

students_data = [
    {"name": "Иван Иванов"},
    {"name": "Анна Смирнова"},
    {"name": "Петр Сидоров"},
    {"name": "Мария Кузнецова"},
]

subjects_data = [
    {"title": "Математика"},
    {"title": "Физика"},
    {"title": "Литература"},
    {"title": "Информатика"},
]

grades_data = [
    {"student_idx": 0, "subject_idx": 0, "value": 4.5},
    {"student_idx": 0, "subject_idx": 1, "value": 3.0},
    {"student_idx": 1, "subject_idx": 0, "value": 5.0},
    {"student_idx": 2, "subject_idx": 2, "value": 4.0},
    {"student_idx": 3, "subject_idx": 3, "value": 3.7},
    {"student_idx": 1, "subject_idx": 3, "value": 4.2},
]

async def populate():
    async with SessionLocal() as session:
        
	# Очистка таблиц
        await session.execute(text("TRUNCATE grades, students, subjects RESTART IDENTITY CASCADE"))
        await session.commit()

	# Добавляем студентов
        student_objs = []
        for s in students_data:
            student = models.Student(name=s["name"])
            session.add(student)
            student_objs.append(student)

        # Добавляем предметы
        subject_objs = []
        for s in subjects_data:
            subject = models.Subject(title=s["title"])
            session.add(subject)
            subject_objs.append(subject)

        await session.commit()
        for student in student_objs:
            await session.refresh(student)
	
        for subject in subject_objs:
            await session.refresh(subject)

        # Добавляем оценки
        for g in grades_data:
            grade = models.Grade(
                student_id=student_objs[g["student_idx"]].id,
                subject_id=subject_objs[g["subject_idx"]].id,
                value=g["value"]
            )
            session.add(grade)

        await session.commit()

if __name__ == "__main__":
    asyncio.run(populate())

