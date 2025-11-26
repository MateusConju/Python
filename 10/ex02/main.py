from fastapi import FastAPI, Depends
from mockdb.database import MockDB
from mockdb.dependencies import get_db

app = FastAPI()

@app.get("/db")
def read_data(db:MockDB = Depends(get_db)):
    return {"data": db.query()}