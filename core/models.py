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
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=300, null=True)
    members_count = models.PositiveIntegerField()
    verified = models.BooleanField(default=False)
    site = models.CharField(max_length=200, null=True)
    photo_100 = models.URLField()

    def __str__(self):
        return f'{self.name} - [{self.vk_id}]'

    class Meta:
        ordering = ('name',)


class VKPost(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    owner = models.ForeignKey(VKGroup, on_delete=models.CASCADE)
    address = models.SlugField(
        max_length=140,
        null=True,
        blank=True
    )
    pub_date = models.DateField()
    text = models.CharField(max_length=3000)
    comments = models.PositiveIntegerField()
    likes = models.PositiveIntegerField()
    reposts = models.PositiveSmallIntegerField()
    checked = models.BooleanField(default=False)
    objects = Manager()
    unchecked = UncheckedVKPost()

    def save(self, *args, **kwargs):
        self.address = f'https://vk.com/{self.owner.id}_{self.id}'
        super(VKPost, self).save(*args, **kwargs)

    class Meta:
        ordering = ('-pub_date',)
