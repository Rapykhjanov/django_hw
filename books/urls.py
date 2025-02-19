from django.urls import path
from .views import BooksListView, BooksDetailView, AboutMeView, TextAndPhotoView, SystemTimeView, SearchView

urlpatterns = [
    path('', BooksListView.as_view(), name='books_list'),
    path('books_detail/<int:id>/', BooksDetailView.as_view(), name='books_detail'),
    path('about_me/', AboutMeView.as_view(), name='about_me'),
    path('text_and_photo/', TextAndPhotoView.as_view(), name='text_and_photo'),
    path('system_time/', SystemTimeView.as_view(), name='system_time'),
    path('search/', SearchView.as_view(), name='search'),
]

















