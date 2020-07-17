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


class UncheckedVKPost(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(checked=False)


class VKSource(models.Model):
    name = models.CharField(max_length=200)
    vk_id = models.CharField(max_length=32, primary_key=True, unique=True)

    def __str__(self):
        return f'{self.name} - [{self.vk_id}]'

    class Meta:
        ordering = ('name',)


class VKGroup(models.Model):
    name = models.CharField(max_length=200)
    vk_id = models.CharField(max_length=32, primary_key=True, unique=True)
    description = models.CharField(max_length=300)
    members_count = models.IntegerField()
    verified = models.BooleanField(default=False)
    site = models.CharField(max_length=200)
    photo_100 = models.URLField()

    def __str__(self):
        return f'{self.name} - [{self.vk_id}]'

    class Meta:
        ordering = ('name',)


class VKPost(models.Model):
    owner_id = models.ForeignKey(VKGroup, on_delete=models.CASCADE)
    pub_date = models.DateField()
    text = models.CharField(max_length=3000)
    comments = models.IntegerField()
    likes = models.IntegerField()
    reposts = models.IntegerField()
    checked = models.BooleanField(default=False)
    objects = Manager()
    unchecked = UncheckedVKPost()

    class Meta:
        ordering = ('-pub_date',)
