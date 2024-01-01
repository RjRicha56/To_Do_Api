import sqlite3
from fastapi import status
from ..models.user import User
from ..models.Response_model import ResponseModel


async def signup(form_val) -> ResponseModel:
    try:
        con = sqlite3.connect('bucket_list.db', timeout=5)
        cur = con.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS LoginNewUser (
                        username TEXT PRIMARY KEY,
                        password TEXT NOT NULL,
                        full_name TEXT,
                        id INTEGER
                        )
                    """)
        cur.execute("""INSERT INTO LoginNewUser
                        VALUES(?,?,?,?)""",(form_val.username,form_val.password,form_val.full_name, form_val.id))
        con.commit()
        con.close()
        return ResponseModel(status="Success", code=status.HTTP_200_OK, details={'status': f"New user created successfully"})
    except sqlite3.IntegrityError:
        return ResponseModel(status=status.HTTP_409_CONFLICT, code="Exist", details={'status': "Email ID already exist"})

async def get_user(u_email):
    con = sqlite3.connect('bucket_list.db', timeout=5)
    cur = con.cursor()
    user = cur.execute(f"""SELECT * FROM LoginNewUser WHERE username='{u_email}' """)
    user_dict = {}
    for value in user:
        print(value)
        user_dict['e_mail'] = value[0]
        user_dict['password'] = value[2]
        user_dict['u_name'] = value[1]
        user_dict['id'] = value[3]
    con.commit()
    con.close()
    return user_dict

