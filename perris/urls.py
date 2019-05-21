from django.urls import path, include
from .views import index, voluntario

urlpatterns = [
     path('', index, name='index'),
     path('registro', voluntario, name='voluntario'),
]