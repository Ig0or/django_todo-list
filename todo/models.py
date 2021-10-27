from django.db import models

# Create your models here.

class Tarefas(models.Model):
    tarefa = models.TextField(null=False, blank=False)