from fastapi import FastAPI
import sys

sys.path.insert(0, 'C:/Users/Richa/PycharmProjects/LNH_Training')
from Services.ToDo_Task.routes import Todo

app = FastAPI()

app.include_router(Todo.router)


@app.get("/Todo_Task/")
def root():
    return {'data': 'values'}
