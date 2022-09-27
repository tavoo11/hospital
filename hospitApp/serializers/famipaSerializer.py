from hospitApp.models.famiPacinete import FamiPaciente
from hospitApp.models.usuario import Usuario
from rest_framework import serializers

from hospitApp.serializers.usuarioSerializer import UsuarioSerializer

class FamipaSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer()
    class Meta:
        model = FamiPaciente
        fields = ['idFamiliar', 'isActivo', 'usuario']

    def create(self, validated_data):
        usuarioData = validated_data.pop('usuario')
        userInstance = Usuario.objects.create(**usuarioData)
        FamiPaciente.objects.create(usuario= userInstance, **validated_data)
        return userInstance

    def to_representation(self, obj):
        usuario = Usuario.objects.get(idUsuario=obj.usuario.idUsuario)
        famiPaciente = FamiPaciente.objects.get(idFamiliar=obj.idFamiliar)
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
            'famiPaciente':{
                'idFamiliar': famiPaciente.idFamiliar,
                'isActivo': famiPaciente.isActivo
            }
        }