from django.contrib import admin

from core.models import YandexNewsTopic


@admin.register(YandexNewsTopic)
class YandexNewsTopicAdmin(admin.ModelAdmin):
    list_display = ['name', 'rss_url']
    search_fields = ['name']
    ordering = ['name']
