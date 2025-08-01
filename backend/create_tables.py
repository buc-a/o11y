import asyncio
from app.database import engine, Base
from app import models 

async def create():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

asyncio.run(create())

