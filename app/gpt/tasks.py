import time

from openai.error import ServiceUnavailableError

from app.celery_app import celery
from app.gpt.service import ChatGPT


@celery.task(
    rate_limit="120/m",
    autoretry_for=(ServiceUnavailableError,),
    retry_kwargs={'max_retries': 3},
    soft_time_limit=60,
    time_limit=65
)
def send_gpt_task(prompt: str):
    return ChatGPT().send_request(prompt)
