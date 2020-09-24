import logging

from django.db import IntegrityError

from core.models import YandexNewsTopic, YandexNewsItem, TriggerPhrase, TriggerNews, VKPost
from core.util.SiteParser import SiteParser
from core.util.ArticleAnalyser import ArticleAnalyser
from core.vk.vk_parser import VKParser
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
                logger.info(f'Added: [{news.hash}] {news.title}')
            except IntegrityError:
                # handling re-adding news
                logger.info(f'Exist: [{news.hash}] {news.title}')


@app.task
def check_yandex_news_for_trigger_words():
    # todo: take all unchecked news
    news = YandexNewsItem.unchecked.all()[:5]  # all() [:5] for testing
    # init site parser
    parser = SiteParser()
    # init analyser
    analyser = ArticleAnalyser()
    # get all trigger words
    trigger_phrase = TriggerPhrase.objects.all()
    # add keywords
    analyser.add_keywords(trigger_phrase)

    for article in news.iterator():
        # get raw article text and article name
        raw_text = parser.get_article_text(article.link)
        article_name = article.title

        article_keywords_found_list = analyser.check_text(raw_text)
        article_name_keywords_found_list = analyser.check_text(article_name)

        if article_keywords_found_list or article_name_keywords_found_list:
            TriggerNews.objects.create(
                title=article.title,
                article_link=article.link,
                description='',
                rate=0
            )
            logger.warning(f'Trigger: [{article.hash}] {article.title}')

        # update article
        article.checked = True
        article.save()
        logger.info(f'Checked: [{article.hash}] {article.title}')

@app.task
def update_vk_content():
    parser = VKParser()
    parser.parse_groups()


@app.task
def check_vk_news_for_trigger_words():
    posts = VKPost.unchecked.all()
    analyser = ArticleAnalyser()
    # get all trigger words
    trigger_phrase = TriggerPhrase.objects.all()
    # add keywords
    analyser.add_keywords(trigger_phrase)
    for post in posts.iterator():
        text = post.text
        article_keywords_found_list = analyser.check_text(text)

        if article_keywords_found_list:
            TriggerNews.objects.create(
                title=post.id,
                article_link=post.address,
                description='',
                rate=0
            )
            logger.warning(f'Trigger: {post.id}')
        post.checked = True
        post.save()
        logger.info(f'VK: {post.id} has been checked')