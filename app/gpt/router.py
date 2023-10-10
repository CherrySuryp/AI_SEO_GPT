import asyncio

from fastapi import APIRouter
from celery.result import AsyncResult

from app.gpt.schema import ResponseSchema
from app.gpt.tasks import send_gpt_task

router = APIRouter(tags=["GPT"])


async def get_celery_result(request):
    while not request.ready():
        await asyncio.sleep(1)
    return request.result


@router.get("/gpt")
async def generate_response(prompt: str):
    request = send_gpt_task.delay(prompt)
    response = await get_celery_result(request)
    return ResponseSchema.model_validate({"response": response})
