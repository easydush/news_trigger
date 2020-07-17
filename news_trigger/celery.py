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
    # update news from rss page
    'add-update-news-items': {
        'task': 'core.tasks.update_news_items',
        # every 5 min
        # todo: update time
        'schedule': crontab(minute='*/5'),
    },
    # task to check news for trigger words
    'add-check-news-for-trigger-words': {
        'task': 'core.tasks.check_yandex_news_for_trigger_words',
        # every minute
        # todo: update time
        'schedule': crontab(minute='*/1'),
    }
}
# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
