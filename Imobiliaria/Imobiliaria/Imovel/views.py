from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from .models import imovel
from .forms import imovelForm   

# Create your views here.
def imovelList(request):
    imoveis = imovel.objects.all().order_by('-created_at')
    return render(request, 'imovel/imovel-list.html',{'imoveis': imoveis})

def imovelView(request, id):
    imoveis = get_object_or_404(imovel, pk=id)
    return render(request, 'imovel/imovel.html', {'imoveis': imoveis})

def cadastrarImovel(request):
    if request.method == 'POST':
        form =  imovelForm(request.POST)

        if form.is_valid():
            imovel = form.save()
            return redirect('/Imovel')

    else:
        form =  imovelForm()
        return render(request, 'imovel/cadastrarImovel.html', {'form': form})
