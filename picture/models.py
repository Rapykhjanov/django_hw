from django.db import models

class Picture(models.Model):
    image = models.ImageField(upload_to="pictures/")
