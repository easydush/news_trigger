from django.contrib import admin

from core.models import YandexNewsTopic, YandexNewsItem, TriggerPhrase


@admin.register(YandexNewsTopic)
class YandexNewsTopicAdmin(admin.ModelAdmin):
    list_display = ['name', 'rss_url']
    search_fields = ['name']
    ordering = ['name']


@admin.register(YandexNewsItem)
class YandexNewsItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'link', 'pub_date', 'checked']
    search_fields = ['title']
    list_filter = ['checked']


@admin.register(TriggerPhrase)
class TriggerPhraseAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
