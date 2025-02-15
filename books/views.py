from django.shortcuts import render
from django.http import HttpResponse
from . import models
from django.shortcuts import get_object_or_404


def books_list(request):
    if request.method == "GET":
        query = models.Books.objects.all().order_by('-id')
        context_object_name = {
            'book_list': query,
        }
        return render(request, template_name='book.html',
                      context=context_object_name)


def books_detail(request, id):
    if request.method == "GET":
        query = get_object_or_404(models.Books, id=id)
        context_object_name = {
            'books_list_id': query,
        }
        return render(request,
                      template_name='book_detail.html',
                      context=context_object_name)



def about_me(request):
    if request.method == "GET":
        return HttpResponse('Привет! Я Сардор , люблю Django!')


def text_and_photo(request):
    if request.method == "GET":
        return HttpResponse(
            'Это моя фотография! <br><img src="https://biopet.az/resized/fit1220x550/center/pages/770/fars-pisiyi-1198x540px.jpg" alt="Фото">')


def system_time(request):
    if request.method == "GET":
        return HttpResponse(f'Текущее время: {now()}')
