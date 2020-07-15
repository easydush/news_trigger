from django.db import models


class YandexNewsTopic(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    rss_url = models.URLField()

    def __str__(self):
        return f'{self.name} - [{self.rss_url}]'

    class Meta:
        ordering = ('name', )
        unique_together = ('name', 'rss_url')
