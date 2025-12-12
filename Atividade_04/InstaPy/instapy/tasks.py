# tasks.py
import time
from database import update_image_status, invalidate_feed_cache, get_image
from redis import Redis
import os
from PIL import Image, ImageFilter

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")

def generate_versions(img_id: str):
    print(f"[worker] Gerando versões da imagem {img_id}")
    # Simula trabalho
    time.sleep(2)  # thumbnail
    time.sleep(2)  # mobile
    time.sleep(2)  # desktop

    versions = {
        "thumbnail_url": f"/media/{img_id}/thumb.jpg",
        "mobile_url": f"/media/{img_id}/mobile.jpg",
        "desktop_url": f"/media/{img_id}/desktop.jpg",
    }
    update_image_status(img_id, "processing_versions", {"versions": versions})
    print(f"[worker] Versões geradas para {img_id}")

def apply_auto_enhance(img_id: str):
    print(f"[worker] Aplicando filtro de melhoria automática em {img_id}")
    time.sleep(3)
    update_image_status(img_id, "processing_filter")
    print(f"[worker] Filtro aplicado em {img_id}")

def finalize_image(img_id: str):
    print(f"[worker] Finalizando {img_id}")
    update_image_status(img_id, "ready")
    invalidate_feed_cache()
    print(f"[worker] Imagem {img_id} pronta e cache invalidado.")

def process_pipeline(img_id: str):
    try:
        generate_versions(img_id)
        apply_auto_enhance(img_id)
        finalize_image(img_id)
    except Exception as e:
        print(f"[worker] Erro no processamento de {img_id}: {e}")
        update_image_status(img_id, "error", {"error": str(e)})
