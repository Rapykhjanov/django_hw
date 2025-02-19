from django.shortcuts import render
from django.views import View
from .models import MarketModel


class MarketView(View):
    def get(self, request):
        context = {}
        try:
            query = MarketModel.objects.all()
            context['market'] = query
        except MarketModel.DoesNotExist:
            context['error'] = 'Не удалось загрузить данные.'

        return render(request, 'market_view.html', context)

