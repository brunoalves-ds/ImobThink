# Generated by Django 2.2.6 on 2019-11-02 00:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Cliente', '0004_remove_cliente_imovel'),
        ('Imovel', '0005_imovel_descricao'),
    ]

    operations = [
        migrations.AddField(
            model_name='imovel',
            name='cliente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Cliente.Cliente'),
        ),
    ]
