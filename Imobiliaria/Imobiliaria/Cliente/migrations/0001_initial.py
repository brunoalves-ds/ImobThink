# Generated by Django 2.2.6 on 2019-10-27 16:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Imovel', '0003_auto_20191021_2030'),
        ('Usuario', '0004_usuario_foto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome Completo')),
                ('genero', models.CharField(choices=[['F', 'Feminino'], ['M', 'Masculino']], max_length=9)),
                ('tipoCliente', models.CharField(choices=[('Locador', 'Locador'), ('Locatário', 'Locatário'), ('Dono', 'Dono'), ('Comprador', 'Comprador')], max_length=20)),
                ('endereco', models.CharField(max_length=300)),
                ('numero', models.CharField(max_length=4)),
                ('bairro', models.CharField(max_length=50)),
                ('cidade', models.CharField(max_length=60)),
                ('UF', models.CharField(choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')], max_length=60)),
                ('CEP', models.CharField(max_length=8)),
                ('email', models.EmailField(max_length=254)),
                ('CPF', models.CharField(max_length=11, unique=True, verbose_name='CPF')),
                ('RG', models.CharField(max_length=7, unique=True)),
                ('nascimento', models.DateField(verbose_name='data de nascimento')),
                ('telefone', models.CharField(max_length=10, unique=True)),
                ('celular', models.CharField(max_length=11, unique=True)),
                ('status', models.CharField(choices=[('Inativado', 'Inativado'), ('Ativado', 'Ativado')], max_length=7)),
                ('informacoes_adicionais', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('imovel', models.ForeignKey(max_length=4, on_delete=django.db.models.deletion.CASCADE, to='Imovel.imovel', verbose_name='Imóvel para Locação')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Usuario.Usuario', verbose_name='Usuario')),
            ],
        ),
    ]
