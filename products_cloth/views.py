from django.shortcuts import render
from django.views import View
from .models import Product

class AllProductsView(View):
    def get(self, request):
        products = Product.objects.all().order_by('id')
        context = {
            'all_products': products,
        }
        return render(request, 'products_cloth/all_products.html', context)


class KidsProductsView(View):
    def get(self, request):
        products = Product.objects.filter(tags__name='для детей').order_by('id')
        context = {
            'kids': products,
        }
        return render(request, 'products_cloth/kids.html', context)


class AdultsProductsView(View):
    def get(self, request):
        products = Product.objects.filter(tags__name='для взрослых').order_by('id')
        context = {
            'adults': products,
        }
        return render(request, 'products_cloth/adults.html', context)


class TeenagerProductsView(View):
    def get(self, request):
        products = Product.objects.filter(tags__name='подростковая').order_by('id')
        context = {
            'teenager': products,
        }
        return render(request, 'products_cloth/teenager.html', context)
































# from django.shortcuts import render
# from. import models
# #Список всех продуктов
# def all_products(request):
#     if request.method == 'GET':
#         query = models.Product.objects.all().order_by('id')
#         context_object_name = {
#             'all_products': query,
#         }
#         return render(request,template_name='products_cloth/all_products.html',
#                       context=context_object_name)
#
#
# #детский
# def kids_products(request):
#     if request.method == 'GET':
#         query = models.Product.objects.filter(tags__name='для детей').order_by('id')
#         context_object_name = {
#             'kids': query,
#         }
#         return render(request,template_name='products_cloth/kids.html',
#                       context=context_object_name)
#
#
# #для взрослых
# def adults_products(request):
#     if request.method == 'GET':
#         query = models.Product.objects.filter(tags__name='для взрослых').order_by('id')
#         context_object_name = {
#             'adults': query,
#         }
#         return render(request,template_name='products_cloth/adults.html',
#                       context=context_object_name)
#
#
# #для подростк
# def teenager_products(request):
#     if request.method == 'GET':
#         query = models.Product.objects.filter(tags__name='подростковая').order_by('id')
#         context_object_name = {
#             'teenager': query,
#         }
#         return render(request,template_name='products_cloth/teenager.html',
#                       context=context_object_name)
