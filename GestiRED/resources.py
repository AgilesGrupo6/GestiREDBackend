from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from tastypie import fields
from .models import *
from tastypie.resources import ALL,  ALL_WITH_RELATIONS



class UserResource(ModelResource):
    rols=fields.ToManyField('GestiRED.resources.RolResource','rols', full=True)

    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        authorization = Authorization()
    #filtro para usuario con roles especificos
        filtering = {
            'rols': ALL_WITH_RELATIONS,
        }



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


class ResourceTypeResource(ModelResource):
    class Meta:
        queryset = ResourceType.objects.all()
        resource_name = 'resourceType'
        authorization = Authorization()

class PhaseTypeResource(ModelResource):
    name = fields.CharField(attribute="name")
    class Meta:
        queryset = PhaseType.objects.all()
        resource_name = 'phaseType'
        authorization = Authorization()



class ResourceResource(ModelResource):

    resourceType = fields.CharField(attribute="resourceType")
    responsibles = fields.ToManyField('GestiRED.resources.UserResource','responsibles')
    #Phases = fields.ToManyField('GestiRED.resources.PhaseResource','resources', null=True)
    class Meta:
        queryset = Resource.objects.all()
        resource_name = 'resource'
        authorization = Authorization()
        filtering = {
            'responsibles': ALL_WITH_RELATIONS,
            'labels': ALL,
        }

    def dehydrate_responsibles(self, bundle):
        user = list ( bundle.obj.responsibles.all ())
        return  [u for u in user]


class PhaseResource(ModelResource):
    phaseType= fields.ForeignKey(PhaseTypeResource, 'phaseType', null=True, full=True, )
    resources = fields.ForeignKey(ResourceResource, 'resource', null=True)
    fields = ['resources']
    class Meta:
        queryset = Phase.objects.all()
        resource_name = 'phase'
        authorization = Authorization()
        filtering = {
            'resources': ALL_WITH_RELATIONS

        }

class Phase2Resource(ModelResource):
    phaseType= fields.ForeignKey(PhaseTypeResource, 'phaseType', null=True, full=True)
    resource = fields.ForeignKey(ResourceResource, 'resource', null=True, full=True)
    fields = ['phaseType']
    class Meta:
        queryset = Phase.objects.all()
        resource_name = 'resources'
        authorization = Authorization()
        filtering = {
            'phaseType': ALL_WITH_RELATIONS

        }


class QualityControlResource(ModelResource):
    responsible  = fields.ForeignKey(UserResource,'responsible', full=True)
    resource = fields.ForeignKey(ResourceResource,'resource', full=True)
    class Meta:
        queryset = QualityControl.objects.all()
        resource_name = 'qualityControl'
        authorization = Authorization()
        filtering = {
            'responsible': ALL_WITH_RELATIONS,
            'resource': ALL_WITH_RELATIONS,
            'state': ALL_WITH_RELATIONS
        }


class ProjectResource(ModelResource):
    resources = fields.ToManyField('GestiRED.resources.ResourceResource',
                                      'resources', full=True)
    class Meta:
        queryset = Project.objects.all()
        resource_name = 'project'
        authorization = Authorization()
        filtering = {
            'resources': ALL_WITH_RELATIONS,
            'labels': ALL,
        }
    #def dehydrate_resources(self, bundle):
    #    resources = list ( bundle.obj.resources.all ())
    #    return  [r for r in resources]


class EventTypeResource(ModelResource):
    class Meta:
        queryset = EventType.objects.all()
        resource_name = 'eventType'
        authorization = Authorization()


class EventResource(ModelResource):
    resource=fields.CharField(attribute="resource")
    eventType =fields.CharField(attribute="eventType")
    user = fields.CharField(attribute="user")
    class Meta:
        queryset = Event.objects.all()
        resource_name = 'event'
        authorization = Authorization()

class CommentsResource(ModelResource):
    resource = fields.ForeignKey(ResourceResource, 'resource', null=True)

    fields = ['resource']
    class Meta:
        queryset = Comments.objects.all()
        resource_name = 'comments'
        authorization = Authorization()
        filtering = {
            'resource': ALL_WITH_RELATIONS

        }

class ResourcexUserResource(ModelResource):

    resourceType = fields.CharField(attribute="resourceType")
    responsibles = fields.ToManyField('GestiRED.resources.UserResource','responsibles')
    #Phases = fields.ToManyField('GestiRED.resources.PhaseResource','resources', null=True)
    class Meta:
        queryset = Resource.objects.all()
        resource_name = 'resourcesxuser'
        authorization = Authorization()
        filtering = {
            'responsibles': ALL_WITH_RELATIONS,
        }

    def dehydrate_responsibles(self, bundle):
        user = list ( bundle.obj.responsibles.all ())
        return  [u for u in user]
