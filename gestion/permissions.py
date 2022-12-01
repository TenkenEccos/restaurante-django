from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.request import Request
from django.contrib.auth.models import AnonymousUser
class SoloAdmin(BasePermission):

    #cambia el mensaje de respuesta
    message = 'No sea Paloma, eso no se puede con sus permisos'
   

    def has_permission(self, request:Request, view):
        #view es la vista a la cual se esta tratando de acceder
        #SAFE_METHODS → es un listado den el cual me muesra los metodos seguros ( los que no afectan la modificacion de datos (GET,OPTIONS, HEAD))
        print(SAFE_METHODS)
        if request.method in SAFE_METHODS:
            #si el metodo que esta utilizando para accede es GET | OPTIONS | HEAD
            return True
        
        if isinstance(request.user , AnonymousUser):
            return False

        if request.user.tipoUsuario == 'ADMIN':
            return True
        else:
            return False