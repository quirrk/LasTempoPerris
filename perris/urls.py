from django.urls import path, include
from .views import index, voluntario, mascotas

urlpatterns = [
     path('', index, name='index'),
     path('registro', voluntario, name='voluntario'),
     path('mascotas', mascotas, name='mascotas'),
]