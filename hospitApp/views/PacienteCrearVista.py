from rest_framework import status, views
#from rest_framework import generics
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from hospitApp.serializers.pacienteSerializer import PacienteSerializer

class PacienteCrearVista(views.APIView):
    #serializer_class = PacienteSerializer
    #queryset = PacienteSerializer.Meta.model.objects.filter()
    def post(self, request, *args, **kwargs):
        serializer = PacienteSerializer(data=request.data)
        serializer.is_valid(raise_exception =True)
        serializer.save()

       # tokenData = { "email":request.data["email"],
       #               "password":request.data["password"]}
        #tokenSerializer = TokenObtainPairSerializer(data=tokenData)
        #tokenSerializer.is_valid(raise_exception= True)

        return Response( status=status.HTTP_201_CREATED)