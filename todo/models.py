from django.db import models
from books.models import Books

class TodoModel(models.Model):
    STATUS_CHOICES = (
        ('Чмтал', 'Читал'),
        ('Не читал', 'Не читал'),
    )
    task = models.CharField(max_length=100)
    choice_books = models.ForeignKey(Books, on_delete=models.CASCADE)
    choice_status = models.CharField(max_length=100, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.task
