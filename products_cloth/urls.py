from django.urls import path
from. import views

urlpatterns =[
    path('all_products/', views.all_products, name='all_products'),
    path('kids/', views.kids_products, name='kids_products'),
    path('adults/', views.adults_products, name='adults_products'),
    path('teenager/', views.teenager_products, name='teenager_products'),
]