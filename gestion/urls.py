from django.urls import path
from .views import *
#me genera la autenticacion
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('registro/',RegistroUsuarioApiView.as_view()),
    path('platos/',PlatosApiView.as_view()),
    path('plato-toggle/<str:id>',PlatoToggleApiView.as_view()),
    path('plato/<int:pk>',PlatoUpdateApiView.as_view()),
    path('iniciar-sesion/',TokenObtainPairView.as_view()),
    path('platos-protegido/',VistaProtegidaPlatosApiView.as_view()),
    path('procedimiento-almacenado/',mostrar_usuarios_raw),
]