from django.contrib import admin

from core.models import YandexNewsTopic, YandexNewsItem, TriggerPhrase, TriggerNews, VKSource, VKGroup, VKPost


@admin.register(YandexNewsTopic)
class YandexNewsTopicAdmin(admin.ModelAdmin):
    list_display = ['name', 'rss_url']
    search_fields = ['name']
    ordering = ['name']


@admin.register(YandexNewsItem)
class YandexNewsItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'hash', 'link', 'pub_date', 'checked']
    search_fields = ['title', 'hash']
    list_filter = ['checked']


@admin.register(TriggerPhrase)
class TriggerPhraseAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(TriggerNews)
class TriggerNewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'article_link', 'last_update', 'rate']
    list_filter = ['last_update', 'rate']
    search_fields = ['title', 'description']
    ordering = ['last_update']


@admin.register(VKSource)
class VKSourceAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(VKGroup)
class VKGroupAdmin(admin.ModelAdmin):
    list_display = ['name', 'id', 'members_count', 'site']
    search_fields = ['name']


@admin.register(VKPost)
class VKPostAdmin(admin.ModelAdmin):
    list_display = ['id', 'owner_id', 'address', 'likes', 'reposts', 'comments', 'checked']
    search_fields = ['id', 'owner_id', 'pub_date']