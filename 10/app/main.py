from fastapi import FastAPI, Depends

app = FastAPI()

def is_workday():
    from datetime import datetime
    return datetime.now().weekday() < 5

@app.get("/work")
def work(is_working:bool = Depends(is_workday)):
    ...