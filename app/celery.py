
from celery import Celery 
import os 
import multiprocessing

if __name__ == "__main__":
    multiprocessing.set_start_method("spawn", force=True)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')

app = Celery('app')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()