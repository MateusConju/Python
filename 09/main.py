from pydantic import BaseModel, Field
from fastapi import FastAPI, Query

app = FastAPI()

@app.get('/items/')
def get_item(store_id:int=0, barcode:int=10):
    return {"store_id": store_id, "barcode": barcode}

@app.get('/search/')
def search_item(q:str = Query(..., max_length=10)):
    return q

class UserSchema(BaseModel):
    username:str
    email:str
    age:int = Field(gt=17)
    is_active:bool = True

@app.put('/user/{user_id}')
def put_user(user_id:int, user_data:UserSchema, wait_for_save:bool = False):
    updated_user = user_data.dict()
    updated_user["id"] = user_id
    return {"updated": updated_user, "wait_for_save": wait_for_save}

