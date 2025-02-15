from django.db import models
from books.models import Books

class MarketModel(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    numbers = models.IntegerField()
    books = models.ManyToManyField(Books)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

