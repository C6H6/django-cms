from django.urls import path

from . import views

app_name = 'travel'

urlpatterns = [
    path('details/<int:travel_id>/', views.details, name='details'),
]
