from pydantic import BaseModel


class TaskList(BaseModel):
    id: int
    task_name: str
    status: str | None
