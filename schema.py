from datetime import date
from pydantic import BaseModel

class User(BaseModel):
    id = int
    username = str
    password = str
    email = str
    adminoruser = int
    

    class Config:
        orm_mode = True


# class Student(BaseModel):
#     name = str
#     number = int




