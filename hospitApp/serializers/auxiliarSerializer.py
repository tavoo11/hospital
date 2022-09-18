
from hospitApp.models.auxiliar import Auxiliar
from rest_framework import serializers

class AuxiliarSerializer(serializers.ModelSerializer):
    class Meta:
         model = Auxiliar
         field = ['idAuxiliar', 'isActivo']
    