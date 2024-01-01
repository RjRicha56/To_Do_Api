from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from ..models.Task import TaskList
from ..modules import task_api, login_api
from ..models import Response_model
from ..models.user import User
from typing import Annotated

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/Todo_Task/login_user/")

@router.post('/save_task/', response_model=Response_model.ResponseModel)
async def save_task(data: TaskList, current_user: Annotated[User, Depends(oauth2_scheme)]):
    print(f'current user: {current_user}')
    response = await task_api.add_data(data,current_user)
    return response


@router.get("/read_task/", response_model=list[TaskList])
async def read_data(current_user: Annotated[User, Depends(oauth2_scheme)]):

    response = await task_api.get_data_from_db(current_user)
    return response


@router.put("/update_status/", response_model=Response_model.ResponseModel)
async def update_data(u_id: int, update_value: str , current_user: Annotated[User, Depends(oauth2_scheme)]):
    response = await task_api.update_value(u_id, update_value,current_user)
    return response


@router.delete("/delete_task/", response_model=Response_model.ResponseModel)
async def delete_data(data_id: int , current_user: Annotated[User, Depends(oauth2_scheme)]):
    response = await task_api.delete_data_from_db(data_id,current_user)
    return response

@router.post("/Signup/", response_model=Response_model.ResponseModel)
async def new_user(data: User):
    response = await login_api.signup(data)
    return response



@router.post("/login_user/")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    '''This is used as the login form'''
    response = await login_api.get_user(form_data.username)
    print(f'response: {response}')
    if not response:
        raise HTTPException(status_code=400, detail="Incorrect username")
    password = form_data.password
    if not password == response["password"]:
        raise HTTPException(status_code=400, detail="Incorrect password")
    return {"access_token": response['id'], "token_type": "bearer"}
