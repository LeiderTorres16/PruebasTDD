from fastapi import FastAPI
from typing import Optional


app = FastAPI()

@app.get("/")
def mensaje():
    return {"Hello World"}

@app.get("/items")
def read_item(item_id:int, q:Optional[str] = None):
        return {"item_id":item_id, "q":q}

@app.post('/posts')
def save_post(post):
    print(post)
    return "recived"
