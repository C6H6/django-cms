from django.urls import path

from . import views

app_name = 'checkout'

urlpatterns = [
    path('add/', views.add, name='add'),
    path('new/', views.new, name='new'),
    path('summary/', views.summary, name='summary'),
    path('remove/<int:offer_id>', views.remove, name='remove'),
]
