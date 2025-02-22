from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import View
from .models import Books
from django.utils.timezone import now
from django.views import generic


# Поиск
class SearchView(generic.ListView):
    template_name = 'book.html'
    context_object_name = 'book_list'

    def get_queryset(self):
        return Books.objects.filter(title__icontains=self.request.GET.get('q'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context


class BooksListView(View):
    def get(self, request):
        books = Books.objects.all().order_by('-id')
        context = {
            'book_list': books,
        }
        return render(request, 'book.html', context)


class BooksDetailView(View):
    def get(self, request, id):
        book = get_object_or_404(Books, id=id)
        context = {
            'book_list_id': book,
        }
        return render(request, 'book_detail.html', context)


class AboutMeView(View):
    def get(self, request):
        return HttpResponse('Привет! Я Сардор , люблю Django!')


class TextAndPhotoView(View):
    def get(self, request):
        return HttpResponse(
            'Это моя фотография! <br><img src="https://biopet.az/resized/fit1220x550/center/pages/770/fars-pisiyi-1198x540px.jpg" alt="Фото">'
        )


class SystemTimeView(View):
    def get(self, request):
        current_time = now()
        return HttpResponse(f'Текущее время: {current_time}')
