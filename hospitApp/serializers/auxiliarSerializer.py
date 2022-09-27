
from hospitApp.models.auxiliar import Auxiliar
from hospitApp.models.usuario import Usuario
from rest_framework import serializers

from hospitApp.serializers.usuarioSerializer import UsuarioSerializer

class AuxiliarSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer
    class Meta:
         model = Auxiliar
         fields = ['idAuxiliar', 'isActivo', 'usuario']

    def create(self, validated_data):
        usuarioData = validated_data.pop('usuario')
        userInstance = Usuario.objects.create(**usuarioData)
        Auxiliar.objects.create(usuario= userInstance, **validated_data)
        return userInstance

    
    def to_representation(self, obj):
        usuario = Usuario.objects.get(idUsuario=obj.usuario.idUsuario)
        auxiliar = Auxiliar.objects.get(idAuxiliar=obj.idAuxiliar)

        return  {
            'idUsuario': usuario.idUsuario,
            'email': usuario.email,
            'password': usuario.password,
            'nombres': usuario.nombres,
            'apellidos': usuario.apellidos,
            'cedula': usuario.cedula,
            'direccion': usuario.direccion,
            'telefono': usuario.telefono,
            'fechaNacimiento': usuario.fechaNacimiento,
            'auxiliar':{
                'idAuxiliar': auxiliar.idAuxiliar,
                'isActivo': auxiliar.isActivo
            }
        }
    