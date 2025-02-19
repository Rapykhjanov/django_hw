from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import TodoModel
from .forms import TodoForm

# Список задач
class TodoListView(ListView):
    model = TodoModel
    template_name = 'todo/todo_list.html'
    context_object_name = 'todo_list'

# Добавление задач
class TodoCreateView(CreateView):
    model = TodoModel
    form_class = TodoForm
    template_name = 'todo/create_todo.html'
    success_url = reverse_lazy('todo_list')


































