from typing import Literal, Optional

from pydantic import BaseModel


class TaskStatus(BaseModel):
    task_id: str = "1d515c0b-45ec-450f-b1ab-a1efffe09c8e"


class TaskResult(BaseModel):
    status: Literal["PENDING", "SUCCESS", "RETRY"] = "PENDING"
    result: Optional[str] = None
