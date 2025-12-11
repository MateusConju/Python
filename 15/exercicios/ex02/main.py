'''
Cenário: Você trabalha em uma Fintech que processa conversões de moedas internacionais. O endpoint atual /convert faz duas coisas:

1. Consulta a Cotação (Externo): Bate em uma API externa de Câmbio para pegar o valor do Dólar atual (Simulado, lento e custoso).

2. Auditoria de Compliance (Log): Se a transação for acima de $10.000, ela precisa ser registrada em um sistema de auditoria de segurança (Simulado, escrita lenta em disco/banco legado).

O Problema: Atualmente, o usuário espera 5 segundos para saber quanto vai receber na conversão. Isso é inaceitável para o mercado financeiro.

Objetivos do Aluno:

Cache no Câmbio (Redis): A cotação do dólar não muda a cada milissegundo. Implemente um cache de 60 segundos para a taxa de câmbio.

Auditoria em Background (Celery): O usuário não precisa esperar o registro da auditoria para ver o resultado. Mova a lógica de audit_compliance para uma Task Assíncrona.
'''

import time
import random

from redis import Redis
from fastapi import FastAPI

from worker import audit_compliance_task

app = FastAPI()
redis_client = Redis(host='localhost', port=6379, decode_responses=True)

def get_external_exchange_rate_with_cache():
    cache_key = "usd_brl_rate"
    cached_rate = redis_client.get(cache_key)

    if cached_rate:
        print("Taxa recurepada via Cache")
        return float(cached_rate)
    
    print("Miss - Consultando API externa")
    time.sleep(2)
    rate = round(random.uniform(4.90, 5.10), 2)

    redis_client.setex(cache_key, 60, str(rate))
    return rate

@app.post("/convert")
def convert_currency(user_id: str, amount_usd: float):
    # Passo 1: Obter taxa (Lento)
    rate = get_external_exchange_rate_with_cache
    
    amount_brl = amount_usd * rate

    audit_status = "Not Required"
    
    # Passo 2: Auditoria se valor alto (Lento)
    if amount_usd > 10000:
        audit_compliance_task.delay(user_id, amount_usd)
        audit_status = "Enviado para a fila"

    return {
        "usd": amount_usd,
        "rate": rate,
        "brl": amount_brl,
        "status": "Success",
        "audit_info": audit_status
    }