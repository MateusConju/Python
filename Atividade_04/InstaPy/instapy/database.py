# database.py
import json
import redis
import os
from typing import List, Dict

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")
rc = redis.from_url(REDIS_URL, decode_responses=True)

IMAGES_SET = "images:set"
FEED_CACHE_KEY = "feed_cache"

def save_image(img_data: Dict):
    img_id = img_data["id"]
    # store json
    rc.set(f"image:{img_id}", json.dumps(img_data))
    rc.sadd(IMAGES_SET, img_id)

def get_image(img_id: str) -> Dict:
    raw = rc.get(f"image:{img_id}")
    return json.loads(raw) if raw else None

def get_all_images() -> List[Dict]:
    ids = rc.smembers(IMAGES_SET) or []
    result = []
    for img_id in ids:
        raw = rc.get(f"image:{img_id}")
        if raw:
            result.append(json.loads(raw))
    # optional: sort by upload timestamp if present
    result.sort(key=lambda x: x.get("uploaded_at", ""), reverse=True)
    return result

def update_image_status(img_id: str, status: str, extra: dict = None):
    img = get_image(img_id)
    if not img:
        return
    img["status"] = status
    if extra:
        img.update(extra)
    rc.set(f"image:{img_id}", json.dumps(img))

def invalidate_feed_cache():
    rc.delete(FEED_CACHE_KEY)

def get_feed_cache():
    raw = rc.get(FEED_CACHE_KEY)
    return json.loads(raw) if raw else None

def set_feed_cache(data, ttl_seconds: int):
    rc.set(FEED_CACHE_KEY, json.dumps(data))
    rc.expire(FEED_CACHE_KEY, ttl_seconds)
