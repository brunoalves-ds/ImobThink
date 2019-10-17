from django import forms

from .models import Task

class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ('nome', 'genero', 'endereco', 'numero', 'bairro', 'cidade', 'UF', 'CEP', 'email', 'CPF', 'RG', 'nascimento','telefone', 'celular', 'status', 'informacoes_adicionais')