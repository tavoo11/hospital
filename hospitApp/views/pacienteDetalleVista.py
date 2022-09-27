from django.conf import settings
from rest_framework import generics, status
#from rest_framework.response import Response
#from rest_framework_simplejwt.backends import TokenBackend
#from rest_framework.permissions import IsAuthenticated

#from hospitApp.models.paciente import Paciente
from hospitApp.serializers.pacienteSerializer import PacienteSerializer

class PacienteDetalleVista (generics.RetrieveAPIView):
    serializer_class = PacienteSerializer
    def get(self):   
        return self.get_serializer().Meta.model.objets.filter(status = True)
    #permission_classes = (IsAuthenticated,)

   

        #token = request.META.get('HTTP_AUTHORIZATION')[7:]
        #tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        #valid_data = tokenBackend.decode(token, verify=False)


        #if valid_data['usuario_idUsuario'] != kwargs['pk']:
        #    stringResponse= {'detail': 'Solicitud no autorizada'}
         #   return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

       