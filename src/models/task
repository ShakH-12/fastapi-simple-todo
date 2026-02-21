from sqlalchemy import (
    Column, String, Integer,
    DateTime
)
from datetime import datetime
from src.database import Base


class Task(Base):
	__tablename__ = "tasks"
	
	id = Column(Integer, primary_key=True, index=True)
	title = Column(String(24), nullable=False, index=True)
	text = Column(String, nullable=True)
	created_at = Column(DateTime, default=datetime.now())

