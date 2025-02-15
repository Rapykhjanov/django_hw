from django.urls import path
from . import views

urlpatterns = [
    path('market_view/', views.market_view, name='market_view'),
]
