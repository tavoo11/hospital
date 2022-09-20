from hospitApp.models.signosVitales import SignosVitales
from rest_framework import serializers

class SignosVSerializer(serializers.ModelSerializer):
    class Meta:
        model = SignosVitales
        fields = ['idSignos', 'presionArterial', 'temperatura', 'frecuenciaCardiaca', 'frecuenciaRespiratoria', 'isActivo']