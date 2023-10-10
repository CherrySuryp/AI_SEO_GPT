from celery import Celery
from app.config import REDIS_URL

celery = Celery(broker=REDIS_URL, backend=REDIS_URL, include=["app.gpt.tasks"])
celery.conf.broker_connection_retry_on_startup = True
