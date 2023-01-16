from django.urls import path
from django.contrib.auth import views as auth_views

from apps.main import views

app_name = 'main'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='main/login.html'), name='login'),
    path('', views.main, name='main')
]
