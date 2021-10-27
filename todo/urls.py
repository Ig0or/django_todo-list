from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('editar/<int:id_tarefa>', editar, name='editar'),
    path('excluir/<int:id_tarefa>', excluir, name='excluir'),
]