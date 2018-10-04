from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from tastypie import fields
from .models import *
from tastypie.resources import ALL,  ALL_WITH_RELATIONS


class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        authorization = Authorization()


class RolResource(ModelResource):
    class Meta:
        queryset = Rol.objects.all()
        resource_name = 'rol'
        authorization = Authorization()


class PrivilegeResource(ModelResource):
    class Meta:
        queryset = Privilege.objects.all()
        resource_name = 'privilege'
        authorization = Authorization()


class PerfilResource(ModelResource):
    role = fields.ForeignKey(RolResource, 'role')
    class Meta:
        queryset = Perfil.objects.all()
        resource_name = 'perfil'
        authorization = Authorization()


class TipoRecursoResource(ModelResource):
    class Meta:
        queryset = TipoRecurso.objects.all()
        resource_name = 'tipoRecurso'
        authorization = Authorization()


class ResourceResource(ModelResource):
    tipoRecurso = fields.ForeignKey(TipoRecursoResource, 'tipoRecurso')
    responsables = fields.ToManyField('GestiRED.resources.UserResource',
                                 'responsables')
    class Meta:
        queryset = Resource.objects.all()
        resource_name = 'resource'
        authorization = Authorization()
        filtering = {
            'responsables': ALL_WITH_RELATIONS,
            'etiquetas': ALL,
        }


class ControlCalidadResource(ModelResource):
    responsable  = fields.ForeignKey(UserResource, 'responsable')
    resource = fields.ForeignKey(ResourceResource, 'resource')
    class Meta:
        queryset = ControlCalidad.objects.all()
        resource_name = 'controlCalidad'
        authorization = Authorization()


class TipoFaseResource(ModelResource):
    class Meta:
        queryset = TipoFase.objects.all()
        resource_name = 'tipoFase'
        authorization = Authorization()


class FaseResource(ModelResource):
    class Meta:
        queryset = Fase.objects.all()
        resource_name = 'fase'
        authorization = Authorization()

class ProjectResource(ModelResource):
    class Meta:
        queryset = Project.objects.all()
        resource_name = 'project'
        authorization = Authorization()


