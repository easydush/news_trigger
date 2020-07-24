from django.db import models
from django.db.models import Manager


class UncheckedYandexNewsItem(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(checked=False)


class YandexNewsTopic(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    rss_url = models.URLField()

    def __str__(self):
        return f'{self.name} - [{self.rss_url}]'

    class Meta:
        ordering = ('name',)
        unique_together = ('name', 'rss_url')


class YandexNewsItem(models.Model):
    title = models.CharField(max_length=300)
    link = models.URLField()
    pub_date = models.DateTimeField()
    hash = models.CharField(max_length=100, unique=True)
    checked = models.BooleanField(default=False)

    objects = Manager()
    unchecked = UncheckedYandexNewsItem()

    def __str__(self):
        return f'{self.title} [{self.pub_date}] [{self.checked}] [{self.hash}] [{self.link}]'


class TriggerPhrase(models.Model):
    name = models.CharField(max_length=300, unique=True)

    def __str__(self):
        return f'{self.name}'


class TriggerNews(models.Model):
    title = models.CharField(max_length=300)
    article_link = models.URLField()
    last_update = models.DateTimeField(auto_now=True)
    description = models.TextField(blank=True)
    rate = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.title} [{self.rate}] - [{self.article_link}]'

    class Meta:
        ordering = ('-last_update',)
        verbose_name = 'Trigger news'
        verbose_name_plural = 'Trigger news'
