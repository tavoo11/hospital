from django.db import models
from .usuario import Usuario

class Medico(models.Model):
    idMedico = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, related_name='medico', on_delete=models.CASCADE)
    isActivo = models.BooleanField(default=True, null=True)
    





































