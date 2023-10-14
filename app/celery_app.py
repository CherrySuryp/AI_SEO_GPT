from celery import Celery
from celery.result import AsyncResult
from fastapi import HTTPException, status

from app.config import REDIS_URL

celery = Celery(broker=REDIS_URL, backend=REDIS_URL, include=["app.gpt.tasks"])
celery.conf.broker_connection_retry_on_startup = True

celery.conf.result_expires = 60


async def get_celery_result(task_id: str):
    task = AsyncResult(task_id)
    if task.state == "PENDING":
        return {"status": "PENDING"}
    elif task.state == "SUCCESS":
        return {"status": "SUCCESS", "result": task.result}
    elif task.state == "FAILURE":
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Task failed after 3 attempts",
        )
    elif task.state == "REVOKED":
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Task was revoked",
        )
    else:
        return {"status": task.state}
