from fastapi import HTTPException

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete

from src.models.task import Task
from src.schemas.task import (
    TaskCreateSchema, TaskResponse,
    TaskListResponse, TaskUpdateSchema,
    TaskDeleteSchema
)


class TaskRepository:
	def __init__(self, db: AsyncSession):
		self.db = db
	
	async def get_all(self):
		tasks = await self.db.execute(select(Task))
		return tasks.scalars().all()
	
	async def get_by_id(self, task_id):
		task = await self.db.execute(select(Task).where(Task.id==task_id))
		return task.scalars().first()
	
	async def create(self, data: TaskCreateSchema):
		task = Task(title=data.title, text=data.text)
		self.db.add(task)
		await self.db.commit()
		await self.db.refresh(task)
		return task
	
	async def update(self, data: TaskUpdateSchema):
		task = await self.db.execute(update(Task).where(Task.id==data.task_id).values(title=data.title, text=data.text))
		task = await self.db.execute(select(Task).where(Task.id==data.task_id))
		await self.db.commit()
		return task.scalars().first()
	
	async def delete(self, data: TaskDeleteSchema):
		await self.db.execute(delete(Task).where(Task.id==data.task_id))
		await self.db.commit()

		