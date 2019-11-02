from django.db import models
from Cliente.models import Cliente

# Create your models here.
class imovel(models.Model): 
    tiposImovel=(
        ('Casa', 'Casa'),
        ('Apartamento','Apartamento'),
        ('kitnet','Kitnet'),
    )
    tiposStatus=(
        ('Ativo','Ativo'),
        ('Inativo','Inativo'),
    )
    tipoImovel = models.CharField(max_length=20, choices=tiposImovel,default='')
    status = models.CharField(max_length=8  , choices=tiposStatus,default='')
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE, null=True
    )
    preco = models.DecimalField(max_digits=19, decimal_places=2)
    cep = models.CharField(max_length=8,default='')
    endereco = models.CharField(max_length=250,default='')
    tamanho = models.PositiveIntegerField()
    quartos = models.PositiveSmallIntegerField()
    andares = models.PositiveSmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    descricao = models.TextField(null=True)
    foto1 = models.ImageField(upload_to='foto_imovel', null=True, blank=True)
    foto2 = models.ImageField(upload_to='foto_imovel', null=True, blank=True)
    foto3 = models.ImageField(upload_to='foto_imovel', null=True, blank=True)
    

    def __str__(self):
        return self.endereco