# Generated by Django 2.2.6 on 2019-10-30 23:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Cliente', '0002_auto_20191029_2053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Usuario.Usuario', verbose_name='Usuario'),
        ),
    ]
