# Generated by Django 5.1.5 on 2025-02-25 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_review_name_alter_review_stars'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='music',
            field=models.FileField(blank=True, null=True, upload_to='music/', verbose_name='Загрузите музыку'),
        ),
    ]
