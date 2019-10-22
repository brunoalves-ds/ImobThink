from django.shortcuts import render, get_object_or_404, redirect
from .models import Usuario
from .forms import NovoUsuarioForm
from django.contrib import messages

# Create your views here.
def listarusuario(request):
    dados = Usuario.objects.all().order_by('-created_at')
    return render(request, 'Usuario/listarUsuario.html', {'dados': dados})


def novousuario(request):
    if request.method == 'POST':
        form = NovoUsuarioForm(request.POST, request.FILES)

        if form.is_valid():
            newuser = form.save()
            return redirect('/Usuario')

    else:
        form = NovoUsuarioForm()
        return render(request, 'Usuario/novoUsuario.html', {'form': form})


def editarusuario(request, id):
    editar = get_object_or_404(Usuario, pk=id)
    form = NovoUsuarioForm(instance=editar)
    if request.method == 'POST':
        form = NovoUsuarioForm(request.POST, request.FILES, instance=editar)
        if form.is_valid():
            editar.save()
            messages.info(request, 'Usuário Editado com Sucesso.')
            return redirect('../../Usuario')
        else:
            return render(request, 'Usuario/editarUsuario.html', {'form': form, 'editar': editar})
    else:
        return render(request, 'Usuario/editarUsuario.html', {'form': form, 'editar': editar})


def excluirusuario(request, id):
    excluir = get_object_or_404(Usuario, pk=id)
    excluir.delete()
    messages.info(request, 'Usuário Deletado com Sucesso.')
    return redirect('../../Usuario')