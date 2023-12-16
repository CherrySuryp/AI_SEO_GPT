from openai.error import ServiceUnavailableError

from app.celery_app import celery
from app.gpt.service import ChatGPT


@celery.task(
    rate_limit="120/m",
    autoretry_for=(ServiceUnavailableError,),
    retry_kwargs={'max_retries': 3},
    default_retry_delay=5,
    soft_time_limit=120,
    time_limit=150
)
def gpt_generate_description_task(prompt: str, model: str):
    gpt = ChatGPT(model=model)
    result = gpt.send_request(prompt).replace("\n", "")
    return result
