from hospitApp.models.paciente import Paciente
from hospitApp.models.usuario import Usuario
from rest_framework import serializers

from hospitApp.serializers.usuarioSerializer import UsuarioSerializer

class PacienteSerializer (serializers.ModelSerializer):
    usuario = UsuarioSerializer()
    class Meta: 
        model = Paciente
        fields = ['idPaciente', 'fechaIngreso', 'fechaSalida', 'isActivo', 'diagnostico', 'usuario']

    def create(self, validated_data):
        usuarioData = validated_data.pop('usuario')
        userInstance = Usuario.objects.create(**usuarioData)
        Paciente.objects.create(usuario= userInstance, **validated_data)
        return userInstance

    def to_representation(self, obj):
        usuario = Usuario.objects.get(idUsuario=obj.usuario.idUsuario)
        paciente = Paciente.objects.get(idPaciente=obj.idPaciente)

        return {
            'usuario':{
            'idUsuario': usuario.idUsuario,
            'email': usuario.email,
            'password': usuario.password,
            'nombres': usuario.nombres,
            'apellidos': usuario.apellidos,
            'cedula': usuario.cedula,
            'direccion': usuario.direccion,
            'telefono': usuario.telefono,
            'fechaNacimiento': usuario.fechaNacimiento,
            },
            'idPaciente': paciente.idPaciente,
            'fechaIngreso': paciente.fechaIngreso,
            'fechaSalida': paciente.fechaSalida,
            'isActivo': paciente.isActivo,
            'diagnostico': paciente.diagnostico
            
        }