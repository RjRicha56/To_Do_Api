from fastapi import APIRouter
from ..models.Task import TaskList
from ..modules import task_api
from ..models import Response_model

router = APIRouter()


@router.post('/save_task/', response_model=Response_model.ResponseModel)
async def save_task(data: TaskList):
    # print('1')
    response = await task_api.add_data(data)
    return response


@router.get("/read_task/", response_model=list[TaskList])
async def read_data():
    response = await task_api.get_data_from_db()
    return response


@router.put("/update_status/", response_model=Response_model.ResponseModel)
async def update_data(u_id: int, update_value: str):
    response = await task_api.update_value(u_id, update_value)
    return response


@router.delete("/delete_task/", response_model=Response_model.ResponseModel)
async def delete_data(data_id: int):
    response = await task_api.delete_data_from_db(data_id)
    return response
