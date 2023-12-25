from pydantic import BaseModel


class ResponseModel(BaseModel):
    status: str
    code: str
    details: dict | None
