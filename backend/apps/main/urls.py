from django.urls import path
from django.contrib.auth import views as auth_views
from .views import UserCreate, AppCreate, Build
from apps.main import views

app_name = 'main'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='main/login.html'), name='login'),
    path('', views.Main.as_view()),
    path('user', UserCreate.as_view()),
    path('app', AppCreate.as_view()),
    path('build', Build.as_view())
]
