from django.shortcuts import render
from django.utils.timezone import now
from django.http import HttpResponse


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