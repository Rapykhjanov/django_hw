from django.urls import path
from .views import MarketView

urlpatterns = [
    path('market_view/', MarketView.as_view(), name='market_view'),
]










