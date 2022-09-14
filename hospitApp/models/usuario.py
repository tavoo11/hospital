# modelado de la base de datos del usuario

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password

class Tipousuario (BaseUserManager):
    def crearUsuario(self, email, password= None):
        """
        Creacion del usuario, utilizando su email y contraseña
        """
        if not email:
            raise ValueError('}El usuario debe tener un correo electronico')
        usuario = self.model(email=email)
        usuario.set_password(password)
        usuario.save(using=self._db)
        return usuario

    def crearSuperUsuario (self, email, password):
        usuario = self.crearUsuario(
            email=email,
            password = password
        )
        usuario._is_admin = True
        usuario.save(using=self._db)
        return usuario




class usuario (AbstractBaseUser):
    idUsuario = models.BigAutoField(primary_key=True)
    email = models.EmailField('correo electronico', unique= True,)
    nombres = models.CharField('nombres', max_length= 100)
    apellidos = models.CharField('apellidos', max_length= 200)
    cedula= models.FloatField('cedula de ciudadania', default=0)
    direccion = models.CharField('direccion', max_length=200)
    telefono = models.IntegerField('Numero celular',default=0)

    def save(self, **kwargs):
        some_salt = 'mMUj0DrIK6vgtdIYepkIxN'
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs)

    objects = Tipousuario()
    EMAIL_FIELD = 'email'



