from time import sleep
import json
import redis
from fastapi import FastAPI

app = FastAPI()

redis_client = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

@app.get("/heavy-games-v2")
def get_heavy_games_cached():
    # ==== Tentar pegar info do Cache ====
    cache_key = "all_games"
    cached_data = redis_client.get(cache_key)

    if cached_data:
        print("Cache Hit!")
        return {"data":json.loads(cached_data), "source":"Redis Cache"}

    # ==== Processar (Lento) ====
    print("Cache Miss - Querying DB...")
    sleep(3)
    data = [{"id":i, "name":f"Game - {i}"} for i in range(10000)]

    # ==== Salvando no Cache ====
    redis_client.setex(cache_key, 15, json.dumps(data))

    return {"data":data, "source":"Database"}

