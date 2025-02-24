from django.db import models
from django.contrib.auth.models import User
from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseBadRequest

child_club = 'Детский клуб'
teenager_club = 'Подростковый клуб'
adult_club = 'Взрослый клуб'

SALARY_RANGES = {
    'no_experience': 30000,
    'junior': 50000,
    'middle': 80000,
}


class CustomUser(User):
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    phone_number = models.CharField(max_length=14, default='+996')
    age = models.PositiveIntegerField(default=7)
    gender = models.CharField(max_length=1, choices=GENDER, default='M')
    club = models.CharField(max_length=100)
    experience = models.PositiveIntegerField(default=0)
    address = models.CharField(max_length=255, blank=True, null=True)
    education = models.CharField(max_length=255, blank=True, null=True)
    skills = models.TextField(blank=True, null=True)
    employment_status = models.CharField(max_length=50, default='Unemployed')
    desired_salary = models.PositiveIntegerField(default=0)
    marital_status = models.CharField(max_length=50, blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.age < 7:
            self.club = 'age must be at least 7'
        elif 7 <= self.age < 12:
            self.club = child_club
        elif 12 <= self.age < 18:
            self.club = teenager_club
        elif 18 <= self.age < 60:
            self.club = adult_club
        else:
            self.club = 'Вы слишком опытны вам это покажется скучным'
        super().save(*args, **kwargs)


class ExperienceSalaryMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path == '/apply/' and request.method == 'POST':
            try:
                experience = int(request.POST.get('experience', 0))
            except ValueError:
                return HttpResponseBadRequest('Некорректное значение опыта')

            if experience < 0:
                return HttpResponseBadRequest('Опыт не может быть отрицательным')
            elif experience == 0:
                request.salary = SALARY_RANGES['no_experience']
            elif 1 <= experience <= 3:
                request.salary = SALARY_RANGES['junior']
            else:
                request.salary = SALARY_RANGES['middle']

        elif request.path == '/apply/' and request.method == 'GET':
            setattr(request, 'salary', 'зарплата не определена')