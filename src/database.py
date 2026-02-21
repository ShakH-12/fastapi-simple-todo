from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase 

from src.config import settings

engine = create_async_engine(settings.database_url)
new_session = async_sessionmaker(engine, expire_on_commit=False)

async def get_session():
	async with new_session() as session:
		yield session

class Base(DeclarativeBase):
	pass

async def create_tables():
	async with engine.begin() as conn:
		await conn.run_sync(Base.metadata.create_all)

