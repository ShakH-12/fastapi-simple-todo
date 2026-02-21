from fastapi import APIRouter, Depends
from src.database import AsyncSession, get_session
from src.services.task import TaskService
from src.schemas.task import TaskCreateSchema, TaskUpdateSchema, TaskDeleteSchema


router = APIRouter(
    prefix="/api/tasks",
    tags=["tasks"]
)

@router.get("")
async def get_tasks(db: AsyncSession = Depends(get_session)):
	service = TaskService(db)
	return await service.get_all()


@router.get("/{task_id}")
async def get_task_by_id(task_id: int, db: AsyncSession = Depends(get_session)):
	service = TaskService(db)
	return await service.get_by_id(task_id)


@router.post("")
async def create(data: TaskCreateSchema, db: AsyncSession = Depends(get_session)):
	service = TaskService(db)
	return await service.create(data)

@router.put("")
async def update(data: TaskUpdateSchema, db: AsyncSession = Depends(get_session)):
	service = TaskService(db)
	return await service.update(data)

@router.delete("")
async def delete(data: TaskDeleteSchema, db: AsyncSession = Depends(get_session)):
	service = TaskService(db)
	return await service.delete(data)

