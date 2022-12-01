from .models import UsuarioModel, PlatoModel
from rest_framework import serializers

class UsuarioSerializer(serializers.ModelSerializer):

    def save(self):
        pass
        #se encarg de guardar el registro en la base de datos
        #1. crea la instancia de nuestro nuevo usuario
        nuevoUsuario = UsuarioModel(**self.validated_data)
        #2.genero el hash de la contraseña
        nuevoUsuario.set_password(self.validated_data.get('password'))
        #3 guardamos el usuario en la base de datos
        nuevoUsuario.save()
        return nuevoUsuario

    class Meta:
        fields = '__all__'
        model = UsuarioModel
        #https://www.django-rest-framework.org/api-guide/serializers/#additional-keyword-arguments 
        # definimos un nuevo atributo llamado kwarg en el cual se realiza mediante un diccionario y se utilizara para indicar parametros adicionales a nuestras columnas
        extra_kwargs ={
            'password':{
                'write_only': True
            },
            'id':{
                'read_only':True
            }
        }

        #con la anterior configuracion estamos indicando que el atributo password solamente sera para escribir mas no para devolver ( read) mientras que el 'id sera solamente para la lectura , mas nunca se podra utilizar para la escritura
class PlatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlatoModel
        fields = '__all__'
        extra_kwargs={
            'disponibilidad':{
                'read_only':True
            }
        }