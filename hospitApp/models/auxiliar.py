from django.db import models
from .usuario import Usuario

class Auxiliar(models.Model):
    idAuxiliar = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, related_name='auxiliar', on_delete=models.CASCADE)
    isActivo = models.BooleanField(default=True)