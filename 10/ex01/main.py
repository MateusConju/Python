from fastapi import FastAPI
from di.dependency import PaginationDep

app = FastAPI()

@app.get("/items")
def list_items(pagination:PaginationDep):
    return {
        "data": ["item1","item2"],
        "meta": pagination
    }