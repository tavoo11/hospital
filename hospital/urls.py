from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from hospitApp import views

urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('user/', views.UsuarioCrearVista.as_view()),
    path('user/<int:pk>/', views.UsuarioDetalleVista.as_view()),
]

