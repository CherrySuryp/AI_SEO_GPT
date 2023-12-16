from typing import Literal

from fastapi import APIRouter, HTTPException, status

from app.celery_app import get_celery_result
from app.gpt.schema import TaskStatus, TaskResult
from app.gpt.tasks import gpt_generate_description_task
from app.config import Config

router = APIRouter(tags=["GPT"])

config = Config()


@router.post("/gpt")
async def generate_description(prompt: str, model: Literal['gpt-4', "gpt-3.5-turbo"] = "gpt-4") -> TaskStatus:
    try:
        task = gpt_generate_description_task.delay(prompt=prompt, model=model)
        return TaskStatus.model_validate({"task_id": task.id})
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Couldn't initiate the task.")


@router.get("/{task_id}/result")
async def get_task_result(task_id: str) -> TaskResult:
    result = await get_celery_result(task_id)
    return result
