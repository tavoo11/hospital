from django.db import models
from .paciente import Paciente

class SignosVitales (models.Model):
    idSignos = models.AutoField(primary_key=True)
    paciente = models.ForeignKey(Paciente, related_name='signosvitales', on_delete=models.CASCADE)
    presionArterial = models.CharField ('presion',max_length=50, null=True)
    temperatura = models.IntegerField(default=0, null=True)
    frecuenciaCardiaca = models.IntegerField(default=0, null=True)
    frecuenciaRespiratoria = models.IntegerField(default=0, null=True)
    isActivo = models.BooleanField(default=True)







