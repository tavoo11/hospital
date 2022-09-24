from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from hospitApp.views.PacienteCrearVista import PacienteCrearVista
from hospitApp.views.pacienteDetalleVista import PacienteDetalleVista
from hospitApp.views.AuxiliarCrearVista import AuxiliarCrearVista
from hospitApp.views.AuxiliarDetalleVista import AuxiliarDetalleVista
from hospitApp.views.familiarCrearVista import FamiliarCrearVista
from hospitApp.views.familiarDetalleVista import FamiliarDetalleVista
from hospitApp.views.medicoCrearVista import MedicoCrearVista
from hospitApp.views.medicoDetalleVista import MedicoDetalleVista


urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('paciente/', PacienteCrearVista.as_view()),
    path('pacientedatos/<int:pk>/', PacienteDetalleVista.as_view()),
    path('auxiliar/', AuxiliarCrearVista.as_view()),
    path('auxiliardatos/<int:pk>/', AuxiliarDetalleVista.as_view()),
    path('familiar/', FamiliarCrearVista.as_view()),
    path('familiardatos/<int:pk>/', FamiliarDetalleVista.as_view()),
    path('medico/', MedicoCrearVista.as_view()),
    path('medicodatos/<int:pk>/', MedicoDetalleVista.as_view()),
]

