from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
from .forms import TaskForm
from django.contrib import messages

from .models import Task


@login_required
def clienteList(request):
    search = request.GET.get('search')
    filter = request.GET.get('filter')

    if search:
        tasks = Task.objects.filter(nome__icontains=search, user=request.user)
    elif filter:
        tasks = Task.objects.filter(status=filter, user=request.user)
    else:
        cliente_list = Task.objects.all().order_by('-created_at').filter(user=request.user)

        paginator = Paginator(cliente_list, 5)

        page = request.GET.get('page')
        tasks = paginator.get_page(page)

    return render(request, 'tasks/list.html', {'tasks': tasks})


@login_required
def clienteView(request, id):
    task = get_object_or_404(Task, pk=id)
    return render(request, 'tasks/task.html', {'task': task})


@login_required
def newCliente(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.status = 'ativo'
            task.user = request.user
            task.save()
            return redirect('/')
    else:
        form = TaskForm()
        return render(request, 'tasks/addtask.html', {'form': form})


@login_required
def editCliente(request, id):
    task = get_object_or_404(Task, pk=id)
    form = TaskForm(instance=task)


    if (request.method == 'POST'):
        form = TaskForm(request.POST, instance=task)

        messages.info(request, 'Cliente editado com sucesso.')

        if (form.is_valid()):
            task.save()
            return redirect('/')
        else:
            return render(request, 'task/edittask.html', {'form': form, 'task': task})
    else:
        return render(request, 'tasks/edittask.html', {'form': form, 'task': task})


@login_required
def deleteCliente(request, id):
    task = get_object_or_404(Task, pk=id)
    task.delete()

    messages.info(request, 'Cliente deletado com sucesso.')

    return redirect('/')



@login_required
def helloWorld(request):
    return HttpResponse('Hello World!')


