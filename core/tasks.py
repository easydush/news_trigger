import logging

from django.db import IntegrityError

from core.models import YandexNewsTopic, YandexNewsItem
from core.yandex_data_export.news_item import NewsItemDownloader
from news_trigger.celery import app

# Get an instance of a logger
logger = logging.getLogger(__name__)


@app.task
def update_news_items():
    # get topics from db
    topics = []

    # test stuff
    # ToDo: add all topics
    test_topic = YandexNewsTopic.objects.get(id=1)
    topics.append(test_topic)
    # end test

    parser = NewsItemDownloader()

    for topic in topics:
        temp_news = parser.get_news_from_rss_page(rss_yandex_link=topic.rss_url)

        for article in temp_news:
            news = YandexNewsItem(
                title=article.title,
                link=article.link,
                pub_date=article.pub_date,
                hash=article.hash
            )
            try:
                news.save()
                logger.info(f'News: {news.title} [{news.hash}] saved')
            except IntegrityError:
                logger.warning(f'News: {news.title} [{news.hash}] already exist')
