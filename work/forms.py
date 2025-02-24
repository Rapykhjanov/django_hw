from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class CustomRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Введите Email')
    phone = forms.CharField(required=True, label='Введите номер телефона')
    age = forms.IntegerField(required=True, label='Укажите ваш возраст')
    gender = forms.ChoiceField(choices=CustomUser.GENDER, label='Укажите ваш пол', required=True)
    address = forms.CharField(required=False, label='Введите ваш адрес')
    education = forms.CharField(required=False, label='Ваше образование')
    skills = forms.CharField(required=False, widget=forms.Textarea, label='Ваши навыки')
    employment_status = forms.CharField(required=False, label='Текущий статус занятости')
    desired_salary = forms.IntegerField(required=False, label='Желаемая зарплата')
    marital_status = forms.CharField(required=False, label='Семейное положение')

    class Meta:
        model = CustomUser
        fields = (
            'username',
            'email',
            'password1',
            'password2',
            'first_name',
            'last_name',
            'age',
            'gender',
            'phone',
            'address',
            'education',
            'skills',
            'employment_status',
            'desired_salary',
            'marital_status',
        )

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.phone_number = self.cleaned_data['phone']
        user.age = self.cleaned_data['age']
        user.gender = self.cleaned_data['gender']
        user.address = self.cleaned_data.get('address', '')
        user.education = self.cleaned_data.get('education', '')
        user.skills = self.cleaned_data.get('skills', '')
        user.employment_status = self.cleaned_data.get('employment_status', '')
        user.desired_salary = self.cleaned_data.get('desired_salary', 0)
        user.marital_status = self.cleaned_data.get('marital_status', '')

        if commit:
            user.save()
        return user
