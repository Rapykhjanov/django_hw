from django.db import models


class Books(models.Model):
    GENRE_CHOICES = (
        ("DRAMA", "DRAMA"),
        ("ROMAN", "ROMAN"),
        ("FANTASY", "FANTASY"),
    )
    image = models.ImageField(upload_to='book_images/', verbose_name='Загрузите фото')
    title = models.CharField(max_length=100, verbose_name="Укажите название книги ")
    description = models.TextField(verbose_name="Укажите описание книги ", blank=True)
    price = models.PositiveIntegerField(verbose_name="Укажите цену ", default=200)
    created_at = models.DateField(auto_now_add=True)
    genre = models.CharField(max_length=10, choices=GENRE_CHOICES, default="DRAMA", verbose_name="Выберите жанр")
    time = models.TimeField(verbose_name="Укажите время ", blank=True, null=True)
    times = models.TimeField(verbose_name="Укажите время просмотра ", blank=True, null=True)
    director = models.CharField(max_length=100, default="Дейл Карнеги")
    trailer = models.URLField(verbose_name="Укажите ссылку из YouTube")
    author = models.CharField(verbose_name="Укажите автора ", max_length=30)
    mail = models.CharField(verbose_name="Укажите почту автора ", max_length=30)

    # Добавляем поле для загрузки музыки
    music = models.FileField(upload_to='music/', verbose_name="Загрузите музыку", blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Книгу"
        verbose_name_plural = "Книги"


class Review(models.Model):
    STARS = (
        ('☀☀', '☀☀'),
        ('☀☀☀', '☀☀☀'),
        ('☀☀☀☀', '☀☀☀☀'),
        ('☀☀☀☀☀', '☀☀☀☀☀'),
    )
    name = models.CharField(max_length=100, verbose_name="Имя пользователя", blank=True, null=True, default="Аноним")
    choices_books = models.ForeignKey(Books, on_delete=models.CASCADE, related_name='books')
    created_at = models.DateField(auto_now_add=True)
    review_text = models.TextField(default="Хорошая книга")
    stars = models.CharField(max_length=10, choices=STARS, default="☀☀☀")

    def __str__(self):
        return f"{self.stars} - {self.choices_books.title}"
