
from django.db import models
from django.contrib.auth import get_user_model

class Task(models.Model):


    STATUS = [
        ('inativo', 'Inativo'),
        ('ativo', 'Ativo'),
    ]

    SEXO_CHOICES = [
        ["F", "Feminino"],
        ["M", "Masculino"],
    ]
    nome = models.CharField(max_length=50, verbose_name='Nome Completo', help_text='Digite seu nome completo')
    genero = models.CharField(max_length=9, choices=SEXO_CHOICES, help_text='Selecione seu gênero')

    imovel = models.CharField(max_length=4, help_text='Informe seu Imovel')
    endereco = models.CharField(max_length=300, help_text='Informe seu endereço')
    numero = models.CharField(max_length=4, help_text='Informe seu Numero')
    bairro = models.CharField(max_length=50, help_text='Informe seu bairro')
    cidade = models.CharField(max_length=60, help_text='Informe sua cidade')
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
    UF = models.CharField(max_length=60, choices=UF, help_text='Selecione seu UF')
    CEP = models.CharField(max_length=8, help_text='Informe seu CEP')

    email = models.EmailField(null=False, help_text='Informe seu E-mail')
    CPF = models.CharField('CPF', max_length=11, unique=True, help_text='Informe seu CPF')
    RG = models.CharField(max_length=7, unique=True, help_text='Informe seu RG')
    nascimento = models.DateField(verbose_name='data de nascimento', help_text='Informe sua data de nascimento')
    telefone = models.CharField(max_length=10, unique=True, help_text='Informe seu telefone')
    celular = models.CharField(max_length=11, unique=True, help_text='Informe seu celular')
    status = models.CharField(max_length=7, choices=STATUS, help_text='Selecione o Status')
    informacoes_adicionais = models.TextField(help_text='Informações adicionais')

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome
