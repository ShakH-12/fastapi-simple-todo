from src.routes.task import router as task_router
from fastapi import APIRouter

main_router = APIRouter()
main_router.include_router(task_router)