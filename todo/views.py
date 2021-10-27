from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import Tarefas


def index(request):
    if request.method == 'POST':
        task = request.POST['tarefa']
        if task:
            Tarefas.objects.create(tarefa=task)
            return redirect(index)
        else:
            todas_tarefas = Tarefas.objects.all()
            return render(request, 'todo/home.html', {'todas_tarefas': todas_tarefas})
    else:
        todas_tarefas = Tarefas.objects.all()
        return render(request, 'todo/home.html', {'todas_tarefas': todas_tarefas})


def editar(request, id_tarefa):
    tarefa_editar = Tarefas.objects.get(id=id_tarefa)
    todas_tarefas = Tarefas.objects.all()
    if request.method == 'POST':
        task = request.POST['tarefa']
        if task:
            Tarefas.objects.filter(id=id_tarefa).update(tarefa=task)
            return redirect(index)
        else:
            return redirect(index)
    return render(request, 'todo/editar.html', {'tarefa': tarefa_editar, 'todas_tarefas': todas_tarefas})

def excluir(request, id_tarefa):
    tarefa_excluir = Tarefas.objects.get(id=id_tarefa)
    tarefa_excluir.delete()
    return redirect(index)
