from django.db import models


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

    def __str__(self):
        return f'{self.title} [{self.pub_date}] [{self.checked}] [{self.hash}] [{self.link}]'
