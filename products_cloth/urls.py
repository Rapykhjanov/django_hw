from django.urls import path
from .views import AllProductsView, KidsProductsView, AdultsProductsView, TeenagerProductsView

urlpatterns = [
    path('all_products/', AllProductsView.as_view(), name='all_products'),
    path('kids/', KidsProductsView.as_view(), name='kids_products'),
    path('adults/', AdultsProductsView.as_view(), name='adults_products'),
    path('teenager/', TeenagerProductsView.as_view(), name='teenager_products'),
]














# from django.urls import path
# from. import views
#
# urlpatterns =[
#     path('all_products/', views.all_products, name='all_products'),
#     path('kids/', views.kids_products, name='kids_products'),
#     path('adults/', views.adults_products, name='adults_products'),
#     path('teenager/', views.teenager_products, name='teenager_products'),
# ]