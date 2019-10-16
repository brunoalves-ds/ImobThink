from django import forms

from .models import imovel

class imovelForm(forms.ModelForm):
    class Meta:
        model = imovel
        fields = ('endereco','tipoImovel','status','preco','cep','quartos','tamanho','andares')