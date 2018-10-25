from django.urls import path, include
from .views import index, form

urlpatterns = [
     path('', index),
     path('formulario/', form)
]