import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView, ListView

from core.models import TriggerNews, TriggerPhrase, YandexNewsTopic


class HomeView(LoginRequiredMixin, TemplateView):
    """
    Main page with all main information
    """
    template_name = 'core/home.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['main_page'] = True
        return context_data


class NewsView(LoginRequiredMixin, ListView):
    """
    Main page with all main information
    """
    template_name = 'core/news.html'
    model = TriggerNews
    paginate_by = 4

    def get_context_data(self, *, object_list=None, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['news_page'] = True
        return context_data


class KeyWords(LoginRequiredMixin, ListView):
    """
    Page with all key words
    """
    template_name = 'core/key_words.html'
    model = TriggerPhrase
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['key_words_page'] = True
        return context_data


class YandexNewsSource(LoginRequiredMixin, ListView):
    """
    Page with yandex news sources
    """

    template_name = 'core/yandex_news.html'
    model = YandexNewsTopic
    paginate_by = 6

    def get_context_data(self, *, object_list=None, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['yandex_source'] = True
        return context_data


class ToggleActiveKeyWorld(LoginRequiredMixin, View):
    """
    Toggle trigger word
    """
    def post(self, request):
        if request.is_ajax():
            word_id = request.POST.get('word_id', None)
            is_active = request.POST.get('is_active', None)
            key_word = TriggerPhrase.objects.get(id=word_id)
            key_word.is_active = is_active
            key_word.save()

            data = {'status': 'ok'}
            return HttpResponse(json.dumps(data), content_type='application/json')
