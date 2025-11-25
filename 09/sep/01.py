from fastapi import FastAPI
from enum import Enum

app = FastAPI()

@app.get("/")
def root():
    return {"Sistema":"Not_Monolith", "Versão":"1.0"}

@app.get("/test/{item_id}")
def get_items(item_id):
    item_type = str(type(item_id))
    return {
        "item_id":item_id,
        "type": item_type
        }

@app.get("/items/{item_id}")
def get_items(item_id:int):
    item_type = str(type(item_id))
    return {
        "item_id":item_id,
        "type": item_type
        }

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

@app.get("/models/{model_name}")
def get_models(model_name:ModelName):
    if model_name is ModelName.alexnet:
        return {"Model Name":model_name.value, "Message":"Deep Learning"}
    if model_name is ModelName.resnet:
        return {"Model Name":model_name.value, "Message":"Computer Vision"}
    return {"Model Name":model_name.value, "Message":"Modelo Válido (Não Tratado)"}