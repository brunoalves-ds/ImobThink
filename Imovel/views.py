from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import imovel
from .forms import imovelForm   
from django.contrib import messages
from Cliente.models import Cliente

# Create your views here.
def imovelList(request):

    search = request.GET.get('search')
    filterStatus = request.GET.get('filterStatus')
    filterAndares = request.GET.get('filterAndares')
    filterTipo = request.GET.get('filterTipo')
    filterQuartos = request.GET.get('filterQuartos')

    if search:
        
        imoveis = imovel.objects.filter(endereco__icontains=search)
    
    elif filterStatus:
        
        imoveis = imovel.objects.filter(status=filterStatus)
    
    elif filterTipo:
        
        imoveis = imovel.objects.filter(tipoImovel=filterTipo)
    
    elif filterAndares:
        
        imoveis = imovel.objects.filter(andares=filterAndares)
    
    elif filterQuartos:
        
        imoveis = imovel.objects.filter(quartos=filterQuartos)    

    else:

        imovel_list = imovel.objects.all().order_by('-created_at')

        paginator = Paginator(imovel_list, 3)

        page = request.GET.get('page')

        imoveis = paginator.get_page(page)

    return render(request, 'imovel/imovel-list.html',{'imoveis': imoveis})

def imovelView(request, id):
    imoveis = get_object_or_404(imovel, pk=id)
    return render(request, 'imovel/imovel.html', {'imoveis': imoveis})

def cadastrarImovel(request):
    if request.method == 'POST':
        form =  imovelForm(request.POST, request.FILES)

        if form.is_valid():
            imovel = form.save()
            return redirect('/Imovel')

    else:
        form =  imovelForm()
        return render(request, 'imovel/cadastrarImovel.html', {'form': form})

def editarImovel(request, id):
    imoveis = get_object_or_404(imovel, pk=id)    
    form =  imovelForm(instance=imoveis)

    if(request.method == 'POST'):
        form =  imovelForm(request.POST, instance=imoveis)

        if(form.is_valid()):
            imoveis = form.save()
            return redirect('/Imovel')
        else:
            return render(request, 'imovel/editarImovel.html', {'form': form}, {'imoveis': imoveis})
    else:
        return render(request, 'imovel/editarImovel.html', {'form': form}, {'imoveis': imoveis})

def deletarImovel(request, id):
    imoveis = get_object_or_404(imovel, pk=id) 
    imoveis.delete()

    messages.info(request, 'Imóvel Deletado com Sucesso!')

    return redirect('/Imovel')