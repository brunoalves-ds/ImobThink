from django import forms

from .models import imovel

class imovelForm(forms.ModelForm):
    class Meta:
        model = imovel
        fields = ('cliente','endereco','tipoImovel','status','preco','cep','quartos','tamanho','andares','descricao','foto1','foto2','foto3')