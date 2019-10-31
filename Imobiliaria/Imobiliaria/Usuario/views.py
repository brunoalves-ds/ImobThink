from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Usuario
from .forms import NovoUsuarioForm
from django.contrib import messages
from django.core.paginator import Paginator

# Create your views here.
@login_required
def listarusuario(request):
    search = request.GET.get('search')
    filter = request.GET.get('filter')


    if search:
        dados = Usuario.objects.filter(Nome_Usuario__icontains=search)
    elif filter:
        dados = Usuario.objects.filter(Tipo_Status_Usuario=filter)
    else:
        usuario_list = Usuario.objects.all().order_by('-created_at').filter()

        paginator = Paginator(usuario_list, 3)

        page = request.GET.get('page')
        dados = paginator.get_page(page)
    return render(request, 'Usuario/listarUsuario.html', {'dados': dados})

@login_required
def novousuario(request):
    if request.method == 'POST':
        form = NovoUsuarioForm(request.POST, request.FILES)

        if form.is_valid():
            newuser = form.save()
            return redirect('/Usuario')

    else:
        form = NovoUsuarioForm()
        return render(request, 'Usuario/novoUsuario.html', {'form': form})

@login_required
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

@login_required
def excluirusuario(request, id):
    excluir = get_object_or_404(Usuario, pk=id)
    excluir.delete()
    messages.info(request, 'Usuário Deletado com Sucesso.')
    return redirect('../../Usuario')

@login_required
def inativado(request):
    dados = Usuario.objects.order_by('-created_at')
    return render(request, 'Usuario/', {'dados': dados})

@login_required
def visualizar(request, id):
    dados = get_object_or_404(Usuario, pk=id)
    return render(request, 'Usuario/visualizar.html', {'dados': dados})

@login_required
def visualizarinativado(request, id):
    dados = get_object_or_404(Usuario, pk=id)
    return render(request, 'Usuario/visualizarinativado.html', {'dados': dados})

