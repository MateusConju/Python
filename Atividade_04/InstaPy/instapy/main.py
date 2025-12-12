# main.py
from fastapi import FastAPI, BackgroundTasks, UploadFile, File, Form
from uuid import uuid4
from time import time
import os
from redis import Redis
from rq import Queue
from database import save_image, get_all_images, get_feed_cache, set_feed_cache
from typing import List
import json

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")
redis_conn = Redis.from_url(REDIS_URL, decode_responses=True)
q = Queue("media-tasks", connection=redis_conn)
from datetime import datetime

app = FastAPI()

CACHE_TTL = 5

@app.post("/upload")
async def upload_image(filename: str = Form(...), file: UploadFile = File(...)):
    img_id = str(uuid4())
    uploaded_at = datetime.utcnow().isoformat()
    image_data = {
        "id": img_id,
        "filename": filename,
        "status": "processing",
        "uploaded_at": uploaded_at,
    }
    save_image(image_data)

    q.enqueue("tasks.process_pipeline", img_id, job_timeout=600) 

    return {"id": img_id, "status": "processing"}

@app.get("/feed")
def get_feed():
    # 1) tenta cache Redis
    cached = get_feed_cache()
    if cached:
        return {"source": "cache", "data": cached}

    data = get_all_images()
    set_feed_cache(data, CACHE_TTL)
    return {"source": "db", "data": data}
