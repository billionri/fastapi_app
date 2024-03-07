from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/list_users")
def read_item(user_input: str, password_input: str):
    user_names = {"user1": "password1", "user2": "password2"}
    if user_input in user_names.keys() and user_names[user_input] == password_input:
        return {"message": "User is authenticated. Welcome user: " + user_input}
    else:
        return {"message": "User is not authenticated."}


@app.post("/items/{item_id}")
def post_item(item_id: int, item: Item):
    return {"item_name_post": item.name, "item_id": item_id, 'message': 'This is post request'}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name_put": item.name, "item_id": item_id}