from dataclasses import field
from rest_framework import serializers
from hospitApp.models.usuario import Usuario
from hospitApp.models.auxiliar import Auxiliar
from hospitApp.models.famiPacinete import FamiPaciente
from hospitApp.models.medico import Medico
from hospitApp.models.paciente import Paciente
from hospitApp.models.signosVitales import SignosVitales
from hospitApp.serializers.auxiliarSerializer import AuxiliarSerializer
from hospitApp.serializers.famipaSerializer import FamipaSerializer
from hospitApp.serializers.medicoSerializer import MedicoSerializer
from hospitApp.serializers.pacienteSerializer import PacienteSerializer
from hospitApp.serializers.signosVSerializer import SignosVSerializer

class UsuarioSerializer(serializers.ModelSerializer):
    auxiliar = AuxiliarSerializer()
    famiPaciente = FamipaSerializer()
    medico = MedicoSerializer()
    paciente = PacienteSerializer()
    signosVitales = SignosVSerializer()
    class Meta:
        model = Usuario
        fields = ['idUsuario', 'email', 'nombres', 'apellidos', 'cedula', 'direccion', 'telefono', 'fechaNacimiento', 
                'auxiliar', 'famiPaciente', 'medico', 'paciente', 'signosVitales']
    
    def create(self, validated_date):
        auxiliarData = validated_date.pop('auxiliar')
        famiPaData = validated_date.pop('famiPaciente')
        medicoData = validated_date.pop('medico')
        pacienteData = validated_date.pop('paciente')
        signosData = validated_date.pop('signosVitales')
        userInstance = Usuario.objects.create(**validated_date)
        Auxiliar.objects.create(usuario=userInstance **auxiliarData)
        FamiPaciente.objects.create(usuario=userInstance **famiPaData)
        Medico.objects.create(usuario=userInstance **medicoData)
        Paciente.objects.create(usuario=userInstance **pacienteData)
        SignosVitales.objects.create(usuario=userInstance **signosData)
        return userInstance

    def to_representation(self, obj):
        usuario = Usuario.objects.get(id=obj.idUsuario)
        auxiliar = Auxiliar.objects.get(id=obj.idAuxiliar)
        famiPaciente = FamiPaciente.objects.get(id=obj.idFamiliar)
        medico = Medico.objects.get(id=obj.idMedico)
        paciente = Paciente.objects.get(id=obj.idPaciente)
        signosvitales = SignosVitales.objects.get(id=obj.idSignos)

        return {
            'idUsuario': usuario.id,
            'email': usuario.email,
            'nombres': usuario.nombres,
            'apellidos': usuario.apellidos,
            'cedula': usuario.cedula,
            'direccion': usuario.direccion,
            'telefono': usuario.telefono,
            'fechaNacimiento': usuario.fechaNacimiento,
            'auxiliar':{
                'idAuxiliar': auxiliar.id,
                'isActivo': auxiliar.isActivo
            },
            'famiPaciente':{
                'idFamiliar': famiPaciente.id,
                'isActivo': famiPaciente.isActivo
            },
            'medico':{
                'idMedico':medico.id,
                'isActivo': medico.isActivo
            },
            'paciente':{
            'idPaciente': paciente.id,
            'fechaIngreso': paciente.fechaIngreso,
            'fechaSalida': paciente.fechaSalida,
            'isActivo': paciente.isActivo,
            'diagnostivo': paciente.diagnostico
            },
            'signosVitales': {
                'idSignos': signosvitales.id,
                'presionArterial': signosvitales.presionArterial,
                'temperatura': signosvitales.temperatura,
                'frecuenciaCardiaca': signosvitales.frecuenciaCardiaca,
                'frecuenciaRespiratoria': signosvitales.frecuenciaRespiratoria,
                'isActivo': signosvitales.isActivo
            }
        }