from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ViewSet

from hospitApp.models.auxiliar import Auxiliar
from hospitApp.serializers.auxiliarSerializer import AuxiliarSerializer

class AuxiliarInfoView(ViewSet):
    def list(self, request):
        auxiliares = Auxiliar.objects.all()
        serializer = AuxiliarSerializer(auxiliares, many=True)
        return Response(serializer.data)


class AuxiliarDetalleVista (generics.RetrieveAPIView):
    queryset = Auxiliar.objects.all()
    serializer_class = AuxiliarSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):

        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token, verify=False)


        if valid_data['usuario_idUsuario'] != kwargs['pk']:
            stringResponse= {'detail': 'Solicitud no autorizada'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

        return super().get(request, *args, **kwargs)