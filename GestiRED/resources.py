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


class TipoRecursoResource(ModelResource):
    class Meta:
        queryset = TipoRecurso.objects.all()
        resource_name = 'tipoRecurso'
        authorization = Authorization()

class TipoFaseResource(ModelResource):
    class Meta:
        queryset = TipoFase.objects.all()
        resource_name = 'tipoFase'
        authorization = Authorization()



class ResourceResource(ModelResource):

    tipoRecurso = fields.CharField(attribute="tipoRecurso")
    responsables = fields.ToManyField('GestiRED.resources.UserResource','responsables')
    #fases = fields.ForeignKey ( FaseResource,'fases' )
    class Meta:
        queryset = Resource.objects.all()
        resource_name = 'resource'
        authorization = Authorization()
        filtering = {
            'responsables': ALL_WITH_RELATIONS,
            'etiquetas': ALL,
        }

    def dehydrate_responsables(self, bundle):
        user = list ( bundle.obj.responsables.all ())
        return  [u for u in user]

class FaseResource(ModelResource):
    tipoFase=fields.CharField(attribute="tipoFase")
    resources = fields.CharField(attribute="resource")

    class Meta:
        queryset = Fase.objects.all()
        resource_name = 'fase'
        authorization = Authorization()

class ControlCalidadResource(ModelResource):
    responsable  = fields.CharField(attribute="responsable")
    resource = fields.CharField(attribute="resource")
    class Meta:
        queryset = ControlCalidad.objects.all()
        resource_name = 'controlCalidad'
        authorization = Authorization()


class ProjectResource(ModelResource):
    resources = fields.ToManyField('GestiRED.resources.ResourceResource',
                                      'resources')
    class Meta:
        queryset = Project.objects.all()
        resource_name = 'project'
        authorization = Authorization()
        filtering = {
            'resources': ALL_WITH_RELATIONS,
            'etiquetas': ALL,
        }
    def dehydrate_resources(self, bundle):
        resources = list ( bundle.obj.resources.all ())
        return  [r for r in resources]


class TipoEventoResource(ModelResource):
    class Meta:
        queryset = TipoEvento.objects.all()
        resource_name = 'tipoEvento'
        authorization = Authorization()

class EventoResource(ModelResource):
    resource=fields.CharField(attribute="resource")
    tipoEvento =fields.CharField(attribute="tipoEvento")
    class Meta:
        queryset = Evento.objects.all()
        resource_name = 'evento'
        authorization = Authorization()