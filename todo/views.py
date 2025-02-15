from django.shortcuts import render, redirect
from . import models, forms
#Список задач
def todo_list(request):
    if request.method == 'GET':
        query = models.TodoModel.objects.all()
        context_object_name = {
            'todo_list': query,
        }
        return render(request, template_name='todo/todo_list.html',
                  context=context_object_name)

#Добавление задач
def create_todo(request):
    if request.method == 'POST':
        form = forms.TodoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = forms.TodoForm()
    return render(request, template_name='todo/create_todo.html'
                  ,context={'form':form})

