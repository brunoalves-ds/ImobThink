# Generated by Django 2.2.6 on 2019-10-16 20:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='Digite seu nome completo', max_length=50, verbose_name='Nome Completo')),
                ('genero', models.CharField(choices=[['F', 'Feminino'], ['M', 'Masculino']], help_text='Selecione seu gênero', max_length=9)),
                ('endereco', models.CharField(help_text='Informe seu endereço', max_length=300)),
                ('numero', models.CharField(help_text='Informe seu Numero', max_length=4)),
                ('bairro', models.CharField(help_text='Informe seu bairro', max_length=50)),
                ('cidade', models.CharField(help_text='Informe sua cidade', max_length=60)),
                ('UF', models.CharField(choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')], help_text='Selecione seu UF', max_length=60)),
                ('CEP', models.CharField(help_text='Informe seu CEP', max_length=8)),
                ('email', models.EmailField(help_text='Informe seu E-mail', max_length=254)),
                ('CPF', models.CharField(help_text='Informe seu CPF', max_length=11, unique=True, verbose_name='CPF')),
                ('RG', models.CharField(help_text='Informe seu RG', max_length=7, unique=True)),
                ('nascimento', models.DateField(help_text='Informe sua data de nascimento', verbose_name='data de nascimento')),
                ('telefone', models.CharField(help_text='Informe seu telefone', max_length=10, unique=True)),
                ('celular', models.CharField(help_text='Informe seu celular', max_length=11, unique=True)),
                ('status', models.CharField(choices=[('inativo', 'Inativo'), ('ativo', 'Ativo')], help_text='Selecione o Status', max_length=7)),
                ('informacoes_adicionais', models.TextField(help_text='Informações adicionais')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]