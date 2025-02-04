from django.shortcuts import render
from django.utils.timezone import now

def about_me(request):
    return render(request, 'about_me.html', {'name': 'Привет! Я Сардор , люблю Django!'})

def text_and_photo(request):
    return render(request, 'text_and_photo.html', {'text': 'Это моя  фотография!', 'photo_url': '/static/photo.jpg'})

def system_time(request):
    return render(request, 'system_time.html', {'time': now()})

