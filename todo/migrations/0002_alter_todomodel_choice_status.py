# Generated by Django 5.1.5 on 2025-02-27 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todomodel',
            name='choice_status',
            field=models.CharField(choices=[('Читал', 'Читал'), ('Не читал', 'Не читал')], max_length=100),
        ),
    ]
