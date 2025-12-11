from time import sleep
from celery import Celery

celery_app = Celery(
    "worker",
    broker="amqp://guest:guest@localhost:5672//",
    backend="redis://localhost:6379/0"
)

@celery_app.task(name="send_email_task")
def send_email_task(email:str):
    sleep(15)
    print(f"E-mail enviado para: {email}")
    return f"Status: Enviado para {email}"