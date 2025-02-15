from django.urls import path
from . import views

urlpatterns = [
    path('todo_list/', views.todo_list,name='todo_list'),
    path('create_todo/', views.create_todo,name='create_todo'),
]