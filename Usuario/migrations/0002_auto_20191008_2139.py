# Generated by Django 2.2.6 on 2019-10-09 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Usuario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tipo_Usuario', models.CharField(choices=[('Administrador', 'Administrador'), ('Funcionário', 'Funcionário')], max_length=13)),
                ('Tipo_Status_USuario', models.CharField(choices=[('Ativado', 'Ativado'), ('Inativado', 'Inativado')], max_length=9)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
