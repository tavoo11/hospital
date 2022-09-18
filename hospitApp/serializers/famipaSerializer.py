from hospitApp.models.famiPacinete import FamiPaciente
from rest_framework import serializers

class FamipaSerializer(serializers.ModelSerializer):
    class Meta:
        model = FamiPaciente
        field = ['idFamiliar', 'isActivo']