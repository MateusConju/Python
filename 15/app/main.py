from fastapi import FastAPI
from .worker import send_email_task

app = FastAPI()

@app.post("/async-email")
async def send_email_async(email:str):
    task = send_email_task.delay(email)
    return {
        "msg": "Processamento iniciado em Background",
        "task_id":task.id,
        "status":"Processing"
    }