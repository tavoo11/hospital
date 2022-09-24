from django.db import models
from .usuario import Usuario

class FamiPaciente(models.Model):
    idFamiliar = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, related_name='famipaciente', on_delete=models.CASCADE)
    isActivo = models.BooleanField(default=True, null=True)