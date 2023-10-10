from typing import Annotated
from fastapi import HTTPException, Header, status
from app.config import config


async def verify_api_key(x_api_key: Annotated[str | None, Header()]):
    if x_api_key != config.X_API_KEY:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Invalid X-Api-Key"
        )
