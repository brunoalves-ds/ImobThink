# Generated by Django 2.2.6 on 2019-10-17 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clientes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='imovel',
            field=models.CharField(default='exit', help_text='Informe seu Imovel', max_length=4),
            preserve_default=False,
        ),
    ]