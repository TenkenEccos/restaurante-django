from django.db import models
#contrib → contributions
#auth_user se encuentra en la aplicacion auth
#AbstractBaseUser → me permite control total en la tabla 'auth_user'
#AbstractUser → me permite control solamente en las columnas de nombre,apellido,correo y password de la tabla 'auth_user'
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .authManager import UsuarioManager

# Create your models here.
class PlatoModel(models.Model):
    id = models.AutoField(primary_key=True , null =False , unique = True)
    nombre = models.CharField(max_length= 50, null= False)
    precio = models.DecimalField(max_digits=5, decimal_places =1 ,null = False)
    disponibilidad = models.BooleanField(default = True)
    #auto_now_add → indica se guarde la hora y fecha actual del servidor cuando se cree un nuevo registro → https://docs.djangoproject.com/en/4.1/ref/models/fields/#datefield
    fechaCreacion = models.DateTimeField(auto_now_add=True, db_column='fecha_creacion')
    
    class Meta:
        db_table = 'platos'
        # ordenar por el precio descendiente
        ordering = ['-precio']

class UsuarioModel(AbstractBaseUser, PermissionsMixin):
    #PermissionsMixin → me sirve para poder modificar los permisos que tendra este usuario al momento de crearse los comandos (python manage.py createsuperuser)
    id = models.AutoField(primary_key= True, unique= True)
    nombre = models.CharField(max_length=50, null= False)
    apellido = models.CharField(max_length=50, null= False)
    # EmailField → espera el formatp ****@****.*** 
    correo= models.EmailField(max_length=80, unique=True, null=False)
    password= models.TextField(null=False)

    tipoUsuario = models.CharField(max_length=50, choices =[
        ('ADMIN','ADMINISTRADOR'),
        ('USER','USUARIO')
        ], db_column= 'tipo_usuario')
    #utilizamos los siguiente atributos si queremos seguir trabajando con el panel administrativo
    is_staff=models.BooleanField(default = True)

    is_active= models.BooleanField(default = True)

    createAt = models.DateTimeField(auto_now_add=True, db_column='created_at') 

    objects = UsuarioManager()
    #sera el campo que depidar el panel adminsitrativo para autorizar al usuario, tiene que ser una columna que sea 'unique'
    USERNAME_FIELD = 'correo'
    #las columna o campos requerido al mommento de crear el usuario por la terminal, osea seran los datos solicitados, no tiene que ir el USERNAME_FIELD puesto que esta ya esta implicitamente colocado
    #tampoco va la contraseña poruqe esa ya esta por defecto
    REQUIRED_FIELDS = ['nombre', 'apellido','tipoUsuario']

    class Meta:
        db_table = 'usuarios'
