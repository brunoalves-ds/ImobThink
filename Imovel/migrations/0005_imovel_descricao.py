# Generated by Django 2.2.6 on 2019-10-30 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Imovel', '0004_auto_20191030_1931'),
    ]

    operations = [
        migrations.AddField(
            model_name='imovel',
            name='descricao',
            field=models.TextField(null=True),
        ),
    ]
