from django.shortcuts import render
from. import models
#Список всех продуктов
def all_products(request):
    if request.method == 'GET':
        query = models.Product.objects.all().order_by('id')
        context_object_name = {
            'all_products': query,
        }
        return render(request,template_name='products_cloth/all_products.html',
                      context=context_object_name)


#детский
def kids_products(request):
    if request.method == 'GET':
        query = models.Product.objects.filter(tags__name='для детей').order_by('id')
        context_object_name = {
            'kids': query,
        }
        return render(request,template_name='products_cloth/kids.html',
                      context=context_object_name)


#для взрослых
def adults_products(request):
    if request.method == 'GET':
        query = models.Product.objects.filter(tags__name='для взрослых').order_by('id')
        context_object_name = {
            'adults': query,
        }
        return render(request,template_name='products_cloth/adults.html',
                      context=context_object_name)


#для подростк
def teenager_products(request):
    if request.method == 'GET':
        query = models.Product.objects.filter(tags__name='подростковая').order_by('id')
        context_object_name = {
            'teenager': query,
        }
        return render(request,template_name='products_cloth/teenager.html',
                      context=context_object_name)
