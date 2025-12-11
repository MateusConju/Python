'''
Cenário do Desafio: Você foi contratado por um E-commerce. Eles têm um endpoint de Relatório de Vendas que:

Calcula o faturamento total (Lento - 5s).

Envia um email para o CEO avisando que o relatório foi gerado (Lento - 3s).

O endpoint atual demora 8s e dá timeout no frontend.

Requisitos do Exercício:

1. O cálculo do relatório deve ser cacheado por 30 segundos (se alguém pedir de novo, vem do cache).

2. O envio de email deve ser totalmente assíncrono (não pode travar a resposta do JSON).

3. A resposta da API deve ser quase imediata.
'''
# Imports nativos
import time
import json

# Imports Externos
from redis import Redis
from fastapi import FastAPI

# Imports Locais
from .worker import notify_ceo_task

app = FastAPI()
redis_client = Redis(host='localhost', port=6379, decode_responses=True)

@app.post("/generate-report")
def generate_report(admin_email: str):
    cache_key = 'daily_report'
    cached_total = redis_client.get(cache_key)

    if cached_total:
        total = float(cached_total)
        source = "Cache"
    else:
        time.sleep(5) 
        total = 15000.00

        redis_client.setex(cache_key, 30, str(total))
        source = "Calculated Now"

    notify_ceo_task(admin_email, total)    
       
    return {"total_revenue": total, "source": source, "email_status": "Aguardando na fila"}