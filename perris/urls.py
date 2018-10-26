from django.urls import path, include
from .views import index, persona_form

urlpatterns = [
     path('', index, name='index'),
     path('formulario/', persona_form, name='persona_crear'),
]