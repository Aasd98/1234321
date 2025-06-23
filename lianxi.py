from datetime import datetime

from pydantic import BaseModel

class User(BaseModel):
    len : int
    name : str
    age : int
    wtime : datetime

quser = {
    'len': 5,
    'name': 'tyu',
    'age': 12,
    'wtime': '2025-06-11 15:28:57',
}

user=User(**quser)
print(user.len)
print(user.name)
print(user.age)
print(user.wtime)

