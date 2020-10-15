from django.urls import path

from core.views import HomeView, NewsView

app_name = 'core'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('news/', NewsView.as_view(), name='news')
]