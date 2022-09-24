from hospitApp.models.signosVitales import SignosVitales
from hospitApp.models.usuario import Usuario
from rest_framework import serializers

from hospitApp.serializers.usuarioSerializer import UsuarioSerializer

class SignosVSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer()
    class Meta:
        model = SignosVitales
        fields = ['idSignos', 'presionArterial', 'temperatura', 'frecuenciaCardiaca', 'frecuenciaRespiratoria', 'isActivo', 'usuario']

    def create(self, validated_data):
        usuarioData = validated_data.pop('usuario')
        userInstance = Usuario.objects.create(**usuarioData)
        SignosVitales.objects.create(usuario= userInstance, **validated_data)
        return userInstance

    def to_representation(self, obj):
        usuario = Usuario.objects.get(id=obj.idUsuario)
        signosvitales = SignosVitales.objects.get(id=obj.idSignos)

        return {
            'idUsuario': usuario.id,
            'email': usuario.email,
            'password': usuario.password,
            'nombres': usuario.nombres,
            'apellidos': usuario.apellidos,
            'cedula': usuario.cedula,
            'direccion': usuario.direccion,
            'telefono': usuario.telefono,
            'fechaNacimiento': usuario.fechaNacimiento,
            'signosVitales': {
                'idSignos': signosvitales.id,
                'presionArterial': signosvitales.presionArterial,
                'temperatura': signosvitales.temperatura,
                'frecuenciaCardiaca': signosvitales.frecuenciaCardiaca,
                'frecuenciaRespiratoria': signosvitales.frecuenciaRespiratoria,
                'isActivo': signosvitales.isActivo
            }
        }

    