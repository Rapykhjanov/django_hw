from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseBadRequest

# Диапазоны зарплат
SALARY_RANGES = {
    'no_experience': 30000,  # Новички
    'junior': 50000,  # 1-3 года
    'middle': 80000,  # 3+ лет
}

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
