from django.urls import path

from . import views

app_name = 'authorization'

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('login-check/', views.check_login, name='login-check'),
    path('registration/', views.user_registration, name='registration'),
    path('registration-check/', views.check_registration, name='registration-check'),
    path('logout/', views.user_logout, name='logout')
]
