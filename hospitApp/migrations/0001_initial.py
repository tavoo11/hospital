# Generated by Django 4.1.1 on 2022-09-14 16:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('idUsuario', models.BigAutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='correo electronico')),
                ('nombres', models.CharField(max_length=100, verbose_name='nombres')),
                ('apellidos', models.CharField(max_length=200, verbose_name='apellidos')),
                ('cedula', models.FloatField(default=0, verbose_name='cedula de ciudadania')),
                ('direccion', models.CharField(max_length=200, verbose_name='direccion')),
                ('telefono', models.IntegerField(default=0, verbose_name='Numero celular')),
                ('fechaNacimiento', models.DateField(verbose_name='Fecha de nacimiento')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('idPaciente', models.AutoField(primary_key=True, serialize=False)),
                ('fechaIngreso', models.DateField()),
                ('fechaSalida', models.DateField()),
                ('isActivo', models.BooleanField(default=True)),
                ('diagnostico', models.CharField(max_length=250, verbose_name='diagnostico')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paciente', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SignosVitales',
            fields=[
                ('idSignos', models.AutoField(primary_key=True, serialize=False)),
                ('presionArterial', models.CharField(max_length=50, verbose_name='presion')),
                ('temperatura', models.IntegerField(default=0)),
                ('frecuenciaCardiaca', models.IntegerField(default=0)),
                ('frecuenciaRespiratoria', models.IntegerField(default=0)),
                ('isActivo', models.BooleanField(default=True)),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='signosvitales', to='hospitApp.paciente')),
            ],
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('idMedico', models.AutoField(primary_key=True, serialize=False)),
                ('isActivo', models.BooleanField(default=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medico', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FamiPaciente',
            fields=[
                ('idFamiliar', models.AutoField(primary_key=True, serialize=False)),
                ('isActivo', models.BooleanField(default=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='famipaciente', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Auxiliar',
            fields=[
                ('idAuxiliar', models.AutoField(primary_key=True, serialize=False)),
                ('isActivo', models.BooleanField(default=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='auxiliar', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
