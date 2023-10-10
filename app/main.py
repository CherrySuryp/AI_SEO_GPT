from fastapi import FastAPI, Depends
from app.gpt.router import router as gpt_router
from app.dependencies import verify_api_key

app = FastAPI(
    title="GPT Description Maker",
    redoc_url=None
)

app.include_router(gpt_router, dependencies=[Depends(verify_api_key)])
