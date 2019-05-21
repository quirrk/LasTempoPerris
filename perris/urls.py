from django.urls import path, include
from .views import index, voluntario,video

urlpatterns = [
     path('', index, name='index'),
     path('registro', voluntario, name='voluntario'),
     path('video', video, name='video'),
]