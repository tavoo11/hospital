from django.db import models
from .paciente import Paciente

class SignosVitales (models.Model):
    idSignos = models.AutoField(primary_key=True)
    paciente = models.ForeignKey(Paciente, related_name='signosvitales', on_delete=models.CASCADE)
    presionArterial = models.CharField ('presion',max_length=50)
    temperatura = models.IntegerField(default=0)
    frecuenciaCardiaca = models.IntegerField(default=0)
    frecuenciaRespiratoria = models.IntegerField(default=0)
    isActivo = models.BooleanField(default=True)







