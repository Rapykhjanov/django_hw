from django.urls import path
from . import views

app_name = "users"
urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),  # Регистрация
    path('login/', views.AuthLoginView.as_view(), name='login'),  # Вход
    path('logout/', views.AuthLogoutView.as_view(), name='logout'),  # Выход
    path('user_list/', views.UserListView.as_view(), name='user_list'),  # Список пользователей
]
