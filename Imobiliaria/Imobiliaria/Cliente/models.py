from django.db import models
from Usuario.models import Usuario
from django.contrib.auth import get_user_model


class Cliente(models.Model):


    STATUS = [
        ('Inativado', 'Inativado'),
        ('Ativado', 'Ativado'),
    ]

    SEXO_CHOICES = [
        ["F", "Feminino"],
        ["M", "Masculino"],
    ]
    UF = (
        ("AC", "Acre"),

        ("AL", "Alagoas"),

        ("AP", "Amapá"),

        ("AM", "Amazonas"),

        ("BA", "Bahia"),

        ("CE", "Ceará"),

        ("DF", "Distrito Federal"),

        ("ES", "Espírito Santo"),

        ("GO", "Goiás"),

        ("MA", "Maranhão"),

        ("MT", "Mato Grosso"),

        ("MS", "Mato Grosso do Sul"),

        ("MG", "Minas Gerais"),

        ("PA", "Pará"),

        ("PB", "Paraíba"),

        ("PR", "Paraná"),

        ("PE", "Pernambuco"),

        ("PI", "Piauí"),

        ("RJ", "Rio de Janeiro"),

        ("RS", "Rio Grande do Sul"),

        ("RO", "Rondônia"),

        ("RR", "Roraima"),

        ("SC", "Santa Catarina"),

        ("SP", "São Paulo"),

        ("SE", "Sergipe"),

        ("TO", "Tocantins"),
    )
    tipoClientes = [
        ('Locador','Locador'),
        ('Locatário', 'Locatário'),
        ('Dono', 'Dono'),
        ('Comprador', 'Comprador'),
    ]
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name='Usuario')
    nome = models.CharField(max_length=50, verbose_name='Nome Completo')
    genero = models.CharField(max_length=9, choices=SEXO_CHOICES)
    tipoCliente = models.CharField(max_length=20, choices=tipoClientes)
    endereco = models.CharField(max_length=300)
    numero = models.CharField(max_length=4)
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=60)
    UF = models.CharField(max_length=60, choices=UF)
    CEP = models.CharField(max_length=8)
    email = models.EmailField(null=False)
    CPF = models.CharField('CPF', max_length=11, unique=True)
    RG = models.CharField(max_length=7, unique=True)
    nascimento = models.DateField(verbose_name='data de nascimento')
    celular = models.CharField(max_length=11, unique=True)
    status = models.CharField(max_length=9, choices=STATUS)
    informacoes_adicionais = models.TextField(blank=True, null=True)
    foto = models.ImageField(upload_to='foto_cliente', null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome
