from django.contrib import admin
from . import models
from PIL import Image
from django import forms
from django.core.exceptions import ValidationError


class ImageForm(forms.ModelForm):
    class Meta:
        model = models.Picture
        fields = ['image']

    def clean(self):
        super().clean()
        image = self.cleaned_data.get('image')

        if image:
            try:
                img = Image.open(image)
                # Проверка на максимальные размеры изображения
                max_width = 2000
                max_height = 2000
                if img.width > max_width or img.height > max_height:
                    raise ValidationError(
                        f"Размер изображения слишком большой! Максимальные размеры: {max_width}x{max_height} пикселей."
                    )

                valid_formats = ["JPEG", "JPG", "PNG"]
                if img.format not in valid_formats:
                    raise ValidationError(f"Недопустимый формат файла! Разрешены только: {', '.join(valid_formats)}.")

            except Exception as e:
                raise ValidationError(f"Ошибка обработки изображения: {e}")

        return self.cleaned_data
