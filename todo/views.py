from django.core.cache import cache
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import TodoModel
from .forms import TodoForm

# Список задач
@method_decorator(cache_page(60 * 15), name='dispatch')
class TodoListView(ListView):
    model = TodoModel
    template_name = 'todo/todo_list.html'
    context_object_name = 'todo_list'

    def get_queryset(self):
        return cache.get_or_set(
            'todos',
            lambda: list(self.model.objects.all().order_by('-id').values()),
            60 * 15
        )

# Добавление задач
class TodoCreateView(CreateView):
    model = TodoModel
    form_class = TodoForm
    template_name = 'todo/create_todo.html'
    success_url = reverse_lazy('todo_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        todos = list(TodoModel.objects.all().order_by('-id').values())
        cache.set('todos', todos, 60 * 15)  # Обновляем кэш сразу после создания новой задачи
        return response
