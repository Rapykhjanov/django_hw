from django.shortcuts import render
from . import models

def market_view(request):
    if request.method == 'GET':
        query = models.MarketModel.objects.all()
        context = {
            'market': query,
        }
        return render(request, template_name='market_view.html', context=context)
