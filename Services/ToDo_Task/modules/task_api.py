import sqlite3
from fastapi import HTTPException, status
from ..models import Task
from .. models.Response_model import ResponseModel


def get_connection():
    connection = sqlite3.connect('bucket_list.db', timeout=5)
    return connection


async def add_data(data) -> ResponseModel:
    # print(f'2 {data}')
    con = get_connection()
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS Task (
                id INTEGER PRIMARY KEY,
                task_name TEXT NOT NULL,
                status TEXT
                )
            """)
    try:
        cur.execute("INSERT INTO Task (id, task_name ,status) VALUES (?, ?, ?)",
                    (data.id, data.task_name, data.status))
        con.commit()
        con.close()
        return ResponseModel(status="Success", code=status.HTTP_200_OK, details={'status': "Data created successfully"})
    except sqlite3.IntegrityError:
        return ResponseModel(status=status.HTTP_409_CONFLICT,code="Exist" ,details={'status':"Already Exists"})


async def get_data_from_db() -> list[Task.TaskList]:
    con = get_connection()
    cur = con.cursor()
    data = cur.execute("""SELECT * FROM Task""")
    update_lst = []
    val = ('id', 'task_name', 'status')
    for value in data:
        dict_value = dict(zip(val, value))
        update_lst.append(dict_value)
    con.commit()
    con.close()
    return update_lst


async def delete_data_from_db(user_id) -> ResponseModel:
    all_data = await get_data_from_db()
    for data in all_data:
        if data["id"] == user_id:
            delete_data(user_id)
            return ResponseModel(status="Success", code="Got the data", details= {"status": "Data deleted successfully"})
    return ResponseModel(status=status.HTTP_404_NOT_FOUND,code="Doesn't exist", details={'status':"Data doesn't exist"} )

def delete_data(u_id):
    '''delete data only if data exist'''
    con = get_connection()
    cur = con.cursor()
    cur.execute(f"""delete FROM Task WHERE id={u_id}""")
    con.commit()
    con.close()


async def update_value(data_id, update_status) -> ResponseModel:
    data = await check_data_availability(data_id)
    if len(data) == 0:
        return ResponseModel(status=status.HTTP_404_NOT_FOUND,code="Doesn't exist", details={'status':"Data doesn't exist"} )
    con = get_connection()
    cur = con.cursor()
    cur.execute(f"""UPDATE Task SET status = '{update_status}' WHERE id={data_id}""")
    new_data = cur.execute(f"""SELECT * FROM Task WHERE id={data_id}""")
    val = ('id', 'task_name', 'status')
    update_lst = []
    for value in new_data:
        dict_value = dict(zip(val, value))
        update_lst.append(dict_value)
    con.commit()
    con.close()
    return ResponseModel(status="Success",code=status.HTTP_200_OK, details={'status': update_lst} )


async def check_data_availability(data_id: int):
    db_data = await get_data_from_db()
    data_to_update = []
    for data in db_data:
        if data['id'] == data_id:
            data_to_update.append(data)
    return data_to_update
