from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from hospitApp.views.PacienteCrearVista import PacienteCrearVista
from hospitApp.views.pacienteDetalleVista import PacienteDetalleVista
from hospitApp.views.AuxiliarCrearVista import AuxiliarCrearVista
from hospitApp.views.AuxiliarDetalleVista import AuxiliarDetalleVista, AuxiliarInfoView
from hospitApp.views.familiarCrearVista import FamiliarCrearVista
from hospitApp.views.familiarDetalleVista import FamiliarDetalleVista, FamiliaresInfoView
from hospitApp.views.medicoCrearVista import MedicoCrearVista
from hospitApp.views.medicoDetalleVista import MedicoDetalleVista, MedicoInfoView
from hospitApp.views.pacienteDetalleVista import PacienteInfoView


urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('paciente/', PacienteCrearVista.as_view()),
    path('pacientedatos/<int:pk>/', PacienteDetalleVista.as_view(), name='datospaciente'),
    path('auxiliar/', AuxiliarCrearVista.as_view()),
    path('auxiliardatos/<int:pk>/', AuxiliarDetalleVista.as_view(), name='datosauxiliar'),
    path('familiar/', FamiliarCrearVista.as_view()),
    path('familiardatos/<int:pk>/', FamiliarDetalleVista.as_view(), name='datosfamiliar'),
    path('medico/', MedicoCrearVista.as_view()),
    path('medicodatos/<int:pk>/', MedicoDetalleVista.as_view(), name='datosmedico'),
    path('pacientesinfo/', PacienteInfoView.as_view({'get': 'list'})),
    path('auxiliaresinfo/', AuxiliarInfoView.as_view({'get': 'list'})),
    path('medicosinfo/', MedicoInfoView.as_view({'get': 'list'})),
    path('familiaresinfo/', FamiliaresInfoView.as_view({'get': 'list'})),
]

