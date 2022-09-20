from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from hospitApp.views.usuarioCrearVista import UsuarioCrearVista
from hospitApp.views.usuarioDetalleVista import UsuarioDetalleVista


urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('user/', UsuarioCrearVista.as_view()),
    path('user/<int:pk>/', UsuarioDetalleVista.as_view()),
]

