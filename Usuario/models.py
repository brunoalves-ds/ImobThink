from django.db import models


# Create your models here.
class Usuario(models.Model):
    Tipos_Usuarios = (
        ('Administrador', 'Administrador'),
        ('Funcionário', 'Funcionário'),
    )

    Tipos_Status_Usuarios = (
        ('Ativado', 'Ativado'),
        ('Inativado', 'Inativado'),
    )

    Tipo_Usuario = models.CharField(
        max_length=13,
        choices=Tipos_Usuarios,)

    Tipo_Status_Usuario = models.CharField(
        max_length=9,
        choices=Tipos_Status_Usuarios,
    )
    Nome_Usuario = models.CharField(max_length=255, default="")
    Login_Usuario = models.CharField(max_length=50, default="")
    Senha_Usuario = models.CharField(max_length=100, default="")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    foto = models.ImageField(upload_to='foto_usuario', null=True, blank=True)

    def __str__(self):
        return self.Nome_Usuario