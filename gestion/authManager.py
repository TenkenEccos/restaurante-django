from django.contrib.auth.models import BaseUserManager
#manager → administrador que se encargara de  la creacion del usuario por comando

class UsuarioManager(BaseUserManager):
    #esta clase mes erivra para indicar como tenemos que crear el usuario cuando se haga por linea de comandos
    def create_superuser(self, correo, nombre, apellido, tipoUsuario, password ):
        #metodo que se mandara a llamar cuando se ejecute el comando 'createsuperuser'
        if not correo:
            raise ValueError('El usuario debe indicar obligatoriamente el correo')
        #normalizo el correo→ aparte de validar el patron de correo, remueve espacios innecesarios (espacios en blanco al inicio y final),lo pasa todo a minuscula
        correoNormalizado = self.normalize_email(correo)

        nuevoUsuario = self.model(correo=correoNormalizado, nombre = nombre , apellido = apellido,tipoUsuario = tipoUsuario, password = password)

        #genera el Hash de la contraseña para que no se guarde de manera original
        #set_password(password) genera un hash de la contraseña usando bcrypt y el algoritmo SHA256
        #https://docs.djangoproject.com/en/4.1/ref/contrib/auth/#django.contrib.auth.models.User.set_password
        nuevoUsuario.set_password(password)
        #la siguiente configuracion seria si aun queremos utilizar el panel administrativo
        #is_superuser → sirve para indicar si el usuario es un usuario maestro y puede tener acceso a todo el panel administrativo
        nuevoUsuario.is_superuser = True
        #is_staff → sirve par aindica si el usuario pertenece al equipo de trabajo y que puede tener acceos al panel administrativo ( el is_staff estara regido por los permisos que puede tener ese usuario)
        nuevoUsuario.is_staff = True
        #sirve para referencia a la base de datos por default en el caso que tengamos varias coenxiones a diferentes base de datos
        #de momento el self._db estara vacio , por lo que usara la base da tos por defecto, dado el caso que tuvieramos mas de una conexion a db, tendriamos que especificar el valor , ejm.: using=otrabase
        #https://stackoverflow.com/questions/57667334/what-is-the-value-of-self-db-by-default-in-django
        nuevoUsuario.save(using=self._db)

      