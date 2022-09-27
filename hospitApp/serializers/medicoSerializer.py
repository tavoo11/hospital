from hospitApp.models.medico import Medico
from hospitApp.models.usuario import Usuario
from rest_framework import serializers

from hospitApp.serializers.usuarioSerializer import UsuarioSerializer

class MedicoSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer()
    class Meta:
        model = Medico
        fields = ['idMedico', 'isActivo', 'usuario']

    def create(self, validated_data):
         usuarioData = validated_data.pop('usuario')
         userInstance = Usuario.objects.create(**usuarioData)
         Medico.objects.create(usuario= userInstance, **validated_data)
         return userInstance

    def to_representation(self, obj):
        usuario = Usuario.objects.get(idUsuario=obj.usuario.idUsuario)
        medico = Medico.objects.get(idMedico=obj.idMedico)
        return {
            'idUsuario': usuario.idUsuario,
            'email': usuario.email,
            'password': usuario.password,
            'nombres': usuario.nombres,
            'apellidos': usuario.apellidos,
            'cedula': usuario.cedula,
            'direccion': usuario.direccion,
            'telefono': usuario.telefono,
            'fechaNacimiento': usuario.fechaNacimiento,
            'medico':{
                'idMedico':medico.idMedico,
                'isActivo': medico.isActivo
            }
        }
