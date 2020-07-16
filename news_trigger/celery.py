import os

from celery import Celery
from celery.schedules import crontab
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'news_trigger.settings')
app = Celery('get_news', broker=settings.CELERY_BROKER_URL)

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object("django.conf:settings", namespace="CELERY")

app.conf.beat_schedule = {
    'add-update-news-items': {
        'task': 'core.tasks.update_news_items',
        # every 5 min
        'schedule': crontab(minute='*/5'),
    },
}
# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
