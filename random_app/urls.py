from django.urls import path
from . import views

urlpatterns = [
    path('random/',views.get_random_number, name='get_random_number'),
]