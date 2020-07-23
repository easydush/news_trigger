import logging

from django.db import IntegrityError

from core.models import YandexNewsTopic, YandexNewsItem, TriggerPhrase
from core.site_parser.site_parser import SiteParser
from core.yandex_data_export.news_item import NewsItemDownloader
from news_trigger.celery import app
import re
from flashtext import KeywordProcessor
import pymorphy2

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
        # get news from single rss page
        temp_news = parser.get_news_from_rss_page(rss_yandex_link=topic.rss_url)

        # creating news items
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
                # handling re-adding news
                logger.warning(f'News: {news.title} [{news.hash}] already exist')


@app.task
def check_yandex_news_for_trigger_words():
    # todo: take all unchecked news
    news = YandexNewsItem.unchecked.all()[:5]  # all() [:5] for testing
    # init site parser
    parser = SiteParser()
    keyword_processor = KeywordProcessor()
    trigger_phrase = TriggerPhrase.objects.all()
    # cleaning trigger phrases from punctuation and adding them to keyword processor
    for t in trigger_phrase:
        keyword_processor.add_keyword(re.sub(r'\W+', ' ', t.name))
    morph = pymorphy2.MorphAnalyzer()

    for article in news.iterator():
        # get raw article text
        raw_text = parser.get_article_text(article.link)
        # cleaning the text
        clean_text = re.sub(r'\W+', ' ', raw_text)
        clean_name = re.sub(r'\W+', ' ', article.name)
        # normalizing the text
        final_text = ''
        final_name = ''
        for word in clean_text.split():
            final_text += morph.parse(word)[0].normal_form
            final_text += ' '
        for word in clean_name.split():
            final_name =+ morph.parse(word)[0].normal_form
            final_name += ' '
        # checking the text and article name for trigger words
        if keyword_processor.extract_keywords(final_text) | keyword_processor.extract_keywords(final_name):
            # todo: if article has keywords
        else:
            # todo: if it doesn't

        # update article
        article.checked = True
        article.save()
        logger.info(f'News: {article} checked')
