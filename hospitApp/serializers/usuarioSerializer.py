from dataclasses import field
from rest_framework import serializers
from hospitApp.models.usuario import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['idUsuario', 'email', 'password', 'nombres', 'apellidos', 'cedula', 'direccion', 'telefono', 'fechaNacimiento']
    
    

    