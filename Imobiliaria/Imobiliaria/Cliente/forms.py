from django import forms
from .models import Cliente

class ClienteForm (forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('usuario','nome','genero','imovel','tipoCliente','endereco',
                  'numero','bairro','cidade','UF','CEP','email','CPF','RG','nascimento',
                  'telefone','celular','status','informacoes_adicionais')