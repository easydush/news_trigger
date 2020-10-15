from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from core.models import TriggerNews


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
