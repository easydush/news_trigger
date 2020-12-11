from django.urls import path

from core.views import HomeView, NewsView, KeyWords, YandexNewsSource

app_name = 'core'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('news/', NewsView.as_view(), name='news'),
    path('key-words/', KeyWords.as_view(), name='key_words'),
    path('yandex-source/', YandexNewsSource.as_view(), name='yandex_source')
]
