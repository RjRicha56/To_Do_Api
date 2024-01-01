from fastapi import FastAPI, Depends, HTTPException, status
import sys
from typing import Annotated
sys.path.insert(0, 'C:/Users/Richa/PycharmProjects/LNH_Training')
from Services.ToDo_Task.routes import Todo
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from Services.ToDo_Task.models.user import User

app = FastAPI()
BASE_URL="Todo_Task"
app.include_router(Todo.router,prefix=f"/{BASE_URL}")

# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/Todo_Task/login_user/")


# async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
#     print(f'token: {token}')
#     user = User(
#         username=token + "fakedecoded", email="john@example.com", full_name="John Doe"
#     )
#     return user


@app.get(f"{BASE_URL}")
def root():
    return {'data': 'current_user'}
# =========================================================================






# fake_users_db = {
#     "johndoe": {
#         "username": "johndoe",
#         "full_name": "John Doe",
#         "email": "johndoe@example.com",
#         "hashed_password": "johndoe",
#         "disabled": False,
#     },
#     "alice": {
#         "username": "alice",
#         "full_name": "Alice Wonderson",
#         "email": "alice@example.com",
#         "hashed_password": "alice2",
#         "disabled": True,
#     },
# }
#
#
# class UserInDB(User):
#     hashed_password: str
#
#
# def fake_decode_token(token):
#     print('44')
#     # This doesn't provide any security at all
#     # Check the next version
#     # user = get_user(fake_users_db, token)
#     if token in fake_users_db:
#         user_dict = fake_users_db[token]
#         user = UserInDB(**user_dict)
#     return user
#
#
# async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
#     print('33')
#     user = fake_decode_token(token)
#     if not user:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Invalid authentication credentials",
#             headers={"WWW-Authenticate": "Bearer"},
#         )
#     return user
#
#
#
# @app.post("/token")
# async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
#     print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@222')
#     user_dict = fake_users_db.get(form_data.username)
#     if not user_dict:
#         raise HTTPException(status_code=400, detail="Incorrect username or password")
#     user = UserInDB(**user_dict)
#     hashed_password = form_data.password
#     if not hashed_password == user.hashed_password:
#         raise HTTPException(status_code=400, detail="Incorrect username or password")
#
#     return {"access_token": user.username, "token_type": "bearer"}
#
#
# @app.get("/users/me")
# async def read_users_me(
#     current_user: Annotated[User, Depends(get_current_user)]
# ):
#     print('11')
#     return current_user
