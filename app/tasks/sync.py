from celery import Celery
import os

celery_app = Celery(
    "tasks",
    broker=os.getenv("REDIS_URL"),
    backend=os.getenv("REDIS_URL")
)

@celery_app.task
def sync_trainings(device_id):
    print(f"Sincronizando entrenamientos para dispositivo {device_id}")
