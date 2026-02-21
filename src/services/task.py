from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from src.models.task import Task
from src.schemas.task import (
    TaskCreateSchema, TaskResponse,
    TaskListResponse, TaskUpdateSchema,
    TaskDeleteSchema
)
from src.repositories.task_repository import TaskRepository


class TaskService:
	def __init__(self, db: AsyncSession):
		self.repository = TaskRepository(db)
	
	async def get_all(self):
		tasks = await self.repository.get_all()
		tasks = [TaskResponse.model_validate(task) for task in tasks]
		return TaskListResponse(tasks=tasks, total=len(tasks))
	
	async def get_by_id(self, task_id):
		task = await self.repository.get_by_id(task_id)
		if not task:
			raise HTTPException(
			    status_code=404,
			    detail=f"Task with id {task_id} not found"
			)
		return TaskResponse.model_validate(task)
	
	async def create(self, data: TaskCreateSchema):
		task = await self.repository.create(data)
		return TaskResponse.model_validate(task)
	
	async def update(self, data: TaskUpdateSchema):
		task = await self.repository.get_by_id(data.task_id)
		if not task:
			raise HTTPException(
			    status_code=404,
			    detail=f"Task with id {task_id} not found"
			)
		task = await self.repository.update(data)
		return TaskResponse.model_validate(task)
	
	async def delete(self, data: TaskDeleteSchema):
		task = await self.repository.get_by_id(data.task_id)
		if not task:
			raise HTTPException(
			    status_code=404,
			    detail=f"Task with id {data.task_id} not found"
			)
		await self.repository.delete(data)
		return HTTPException(status_code=201, detail="Deleted")
