from django.shortcuts import render, get_object_or_404, redirect
# Importando Form e Models do Usuario
from Usuario.models import Usuario
# Importando Form e Models do Imóvel
from Imovel.forms import imovelForm
from Imovel.models import imovel
from django.contrib import messages


def principal(request):
    dados = Usuario.objects.filter(Tipo_Status_Usuario='Ativado')
    return render(request, 'dash.html', {'dados': dados})