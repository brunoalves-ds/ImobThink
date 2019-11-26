from django import forms
from .models import Cliente

class ClienteForm (forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('usuario','nome','genero','tipoCliente','endereco',
                  'numero','bairro','cidade','UF','CEP','email','CPF','RG','nascimento','celular','status','informacoes_adicionais','foto')