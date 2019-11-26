from django import forms

from .models import Usuario


class NovoUsuarioForm(forms.ModelForm):

    class Meta:
        model = Usuario
        widgets = {
            'Senha_Usuario': forms.PasswordInput(),
        }
        fields = ('Tipo_Usuario', 'Tipo_Status_Usuario', 'Nome_Usuario', 'Login_Usuario', 'Senha_Usuario', 'foto')
