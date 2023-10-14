from typing import Optional, Literal

from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel

from app.celery_app import get_celery_result
from app.gpt.tasks import send_gpt_task

router = APIRouter(tags=["GPT"])


class TaskStatus(BaseModel):
    task_id: str = "1d515c0b-45ec-450f-b1ab-a1efffe09c8e"


class TaskResult(BaseModel):
    status: Literal["PENDING", "SUCCESS", "RETRY"] = "PENDING"
    result: Optional[str] = None


@router.post("/gpt")
async def send_gpt_task(prompt: str) -> TaskStatus:
    try:
        task = send_gpt_task.delay(prompt=prompt)
        return TaskStatus.model_validate({"task_id": task.id})
    except Exception as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Couldn't initiate the task.")


@router.get("/{task_id}/result")
async def get_task_result(task_id: str) -> TaskResult:
    result = await get_celery_result(task_id)
    return result
