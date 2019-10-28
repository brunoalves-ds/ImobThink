from django.shortcuts import render, get_object_or_404, redirect
from .models import Cliente
from .forms import ClienteForm
from django.contrib import messages
from Usuario.models import Usuario
from Imovel.models import imovel

# Create your views here.
def listarcliente(request):
    tasks = Cliente.objects.all()
    return render(request, 'Cliente/listarCliente.html', {'tasks': tasks})


def visualizarcliente(request, id):
    tasks = get_object_or_404(Cliente, pk=id)
    return render(request, 'Cliente/visualizar.html', {'tasks': tasks})

def visualizarusuario(request, nome):
    dados = get_object_or_404(Usuario, Nome_Usuario=nome )
    return render(request, 'Usuario/visualizar.html', {'dados':dados})

def visualizarimovel(request,nome):
    imoveis = get_object_or_404(imovel, endereco=nome)
    return render(request,'Imovel/imovel.html', {'imoveis': imoveis})

def novocliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)

        if form.is_valid():
            novocliente = form.save()
            return redirect('/Cliente')

    else:
        form = ClienteForm()
        return render(request, 'Cliente/novocliente.html', {'form': form})

def editarcliente(request, id):
    editar = get_object_or_404(Cliente, pk=id)
    form = ClienteForm(instance=editar)
    if request.method == 'POST':
        form = ClienteForm(request.POST, request.FILES, instance=editar)
        if form.is_valid():
            editar.save()
            messages.info(request, 'Cliente Editado com Sucesso.')
            return redirect('../')
        else:
            return render(request, 'Cliente/editarcliente.html', {'form': form, 'editar': editar})
    else:
        return render(request, 'Cliente/editarcliente.html', {'form': form, 'editar': editar})

def excluircliente(request, id):
    excluir = get_object_or_404(Cliente, pk=id)
    excluir.delete()
    messages.info(request, 'Cliente Deletado com Sucesso.')
    return redirect('../../Cliente')


