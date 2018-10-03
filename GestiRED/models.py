from django.db import models


# Create your models here.

class Privilege(models.Model):
    name = models.CharField(max_length=200)


class Rol(models.Model):
    name = models.CharField(max_length=200)
    privileges = models.ManyToManyField(Privilege)


class Perfil(models.Model):
    name = models.CharField(max_length=200)
    role = models.ForeignKey(Rol, on_delete=models.CASCADE)


class User(models.Model):
        name = models.CharField(max_length=200)
        apellido = models.CharField(max_length=200)
        email = models.CharField(max_length=200)
        password = models.CharField(max_length=200)
        fechaRegistro = models.DateTimeField('Date')
        perfiles =  models.ManyToManyField(Perfil)


def __str__(self):
    return '%s %s' % (self.name, self.body)


class TipoRecurso(models.Model):
    nombre = models.CharField(max_length=200)


class Resource(models.Model):
    nombre = models.CharField(max_length=200)
    etiquetas = models.CharField(max_length=2000)
    fechaRegistro = models.DateTimeField('Date')
    url = models.CharField(max_length=200)
    tipoRecurso = models.ForeignKey(TipoRecurso, on_delete=models.CASCADE)
    responsables = models.ManyToManyField('User')


class ControlCalidad(models.Model):
    observacion = models.CharField(max_length=200)
    responsable = models.ForeignKey(User, on_delete=models.CASCADE)
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)


class TipoFase(models.Model):
    nombre = models.CharField(max_length=200)


class Fase(models.Model):
    fechaInicial = models.DateTimeField('Date')
    fechaFinal = models.DateTimeField('Date')
    tipoFase =  models.ForeignKey(TipoFase, on_delete=models.CASCADE)
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)


class Project(models.Model):
    name = models.CharField(max_length=200)
    etiquetas = models.CharField(max_length=2000)
    fechaRegistro = models.DateTimeField('Date')
    resources = models.ManyToManyField(Resource)

