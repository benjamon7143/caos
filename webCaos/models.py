from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
now=datetime.now()

# Create your models here.
class Usuario(models.Model):
    IDUsuario=models.AutoField(primary_key=True)
    NombreUsu=models.CharField(max_length=50)

    def __str__(self) -> str:
        return super().__str__()

class Administrador(models.Model):
    IDAdmin=models.AutoField(primary_key=True)
    NombreAdm=models.CharField(max_length=50)

    def __str__(self) -> str:
        return super().__str__()

class Periodista(models.Model):
    IDPer=models.AutoField(primary_key=True)
    NombrePer=models.CharField(max_length=50)
    ApellidoPer=models.CharField(max_length=50)

    def __str__(self) -> str:
        return super().__str__()

class Categoria(models.Model):
    IDCate=models.AutoField(primary_key=True)
    NombreCate=models.CharField(max_length=50)
    Foto=models.ImageField(upload_to='fotos',null=True)

    def __str__(self) -> str:
        return super().__str__()

class Noticia(models.Model):
    IDNot=models.AutoField(primary_key=True)
    Titulo=models.CharField(max_length=100)
    Descrip=models.TextField(max_length=1000)
    Fecha=models.DateField(now.date())
    categoria=models.ForeignKey(Categoria,on_delete=models.CASCADE)
    periodista=models.ForeignKey(Periodista,on_delete=models.CASCADE)
    Foto=models.ImageField(upload_to='fotos',null=True)
    Publicado=models.BooleanField(default=False)

    def __str__(self) -> str:
        return super().__str__()
    
class Galeria(models.Model):
    IDFoto=models.AutoField(primary_key=True)
    Foto=models.ImageField(upload_to='galeria',null=True)
    Noticia=models.ForeignKey(Noticia,on_delete=models.CASCADE)

