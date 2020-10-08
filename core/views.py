from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView(LoginRequiredMixin, TemplateView):
    """
    Main page with all main information
    """
    template_name = 'core/home.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['main_page'] = True
        return context_data
