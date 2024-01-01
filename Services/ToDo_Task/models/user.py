from pydantic import BaseModel


class User(BaseModel):
    username: str | None
    full_name: str | None
    password: str
    id: int
