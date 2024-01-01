from pydantic import BaseModel


class TaskList(BaseModel):
    id: int
    u_id: int
    task_name: str
    status: str | None
