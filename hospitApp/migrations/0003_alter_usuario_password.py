# Generated by Django 4.1.1 on 2022-09-21 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitApp', '0002_alter_auxiliar_isactivo_alter_famipaciente_isactivo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='password',
            field=models.CharField(max_length=100, verbose_name='contraseña'),
        ),
    ]
