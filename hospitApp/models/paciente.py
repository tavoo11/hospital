from django.db import models
from .usuario import Usuario

class Paciente (models.Model):
    idPaciente = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, related_name='paciente', on_delete=models.CASCADE)
    fechaIngreso = models.DateField()
    fechaSalida = models.DateField()
    isActivo = models.BooleanField(default=True)
    diagnostico = models.CharField ('diagnostico', max_length=250)
    






























































































































































































































































































































































































































