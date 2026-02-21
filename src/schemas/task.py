from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class TaskBase(BaseModel):
	title: str = Field(..., min_length=5, max_length=24)
	text: Optional[str] = Field(None)


class TaskCreateSchema(TaskBase):
	pass


class TaskUpdateSchema(TaskBase):
	task_id: int = Field(ge=0)


class TaskDeleteSchema(BaseModel):
	task_id: int = Field(ge=0)


class TaskResponse(TaskBase):
	id: int = Field(ge=0)
	created_at: datetime
	
	class Config:
		from_attributes = True


class TaskListResponse(BaseModel):
	tasks: list[TaskResponse]
	total: int = Field(ge=0)


	