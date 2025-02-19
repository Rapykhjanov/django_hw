from django.urls import path
from . import views
from .views import TodoListView, TodoCreateView


urlpatterns = [
    path('todo_list/', TodoListView.as_view(), name='todo_list'),
    path('create_todo/', TodoCreateView.as_view(), name='create_todo'),
]





