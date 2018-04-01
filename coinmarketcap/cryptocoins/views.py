from django.shortcuts import render
from django.views.generic import TemplateView

from cryptocoins.models import Cryptocurrency


class CryptocurrenciesTableView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['coins'] = Cryptocurrency.objects.all().order_by('rank')
        return context
