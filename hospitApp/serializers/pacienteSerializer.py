from hospitApp.models.paciente import Paciente
from rest_framework import serializers

class PacienteSerializer (serializers.ModelSerializer):
    class Meta: 
        model = Paciente
        fields = ['idPaciente', 'fechaIngreso', 'fechaSalida', 'isActivo', 'diagnostico']