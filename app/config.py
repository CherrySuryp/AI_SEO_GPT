import os
from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict

dir_path = os.path.dirname(os.path.realpath(__file__))


class Config(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "../.env"
        )
    )

    MODE: Literal["DEV", "PROD"]
    USE_SENTRY: Literal["TRUE", "FALSE"]
    SENTRY_DSN: str

    OPENAI_KEY: str
    RPM_LIMIT: int
    GPT_MODEL: str


config = Config()

if Config().MODE == "PROD":
    REDIS_URL = "redis://redis_ai_seo_gpt:6379/0"

else:
    REDIS_URL = "redis://127.0.0.1:6379/0"

