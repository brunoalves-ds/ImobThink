from django.shortcuts import render, get_object_or_404, redirect
from Usuario.models import Usuario
from django.contrib.auth.decorators import login_required
# Importando Form e Models do Imóvel

from Imovel.models import imovel
from django.contrib import messages
import matplotlib.pyplot as plt

@login_required
def principal(request):
    dados = Usuario.objects.filter(Tipo_Status_Usuario='Ativado')
    x = [6, 7, 4, 5]  # Base
    y = [2, 6, 2, 9]  # Altura

    titulo = "Hello World"
    eixox = "Eixo X"
    eixoy = "Eixo Y"

    grafico = plt.title(titulo)
    grafico = plt.xlabel(eixox)
    grafico = plt.ylabel(eixoy)
    grafico = plt.bar(x,y)
    grafico = plt.savefig('media/grafico/graficos.png', dpi=1200)
    return render(request, 'dash.html', {'dados': dados, 'grafico': grafico})