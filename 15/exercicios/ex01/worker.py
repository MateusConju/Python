from time import sleep
from celery import Celery

celery = Celery(
    "challenge_worker",
    broker="amqp://guest:guest@localhost:5672//",
    backend="redis://localhost:6379/0"
)

@celery.task
def notify_ceo_task(email:str, total_value:float):
    sleep(3)
    print(f"Notificação: Relatório de R$ {total_value} enviado para {email}")
