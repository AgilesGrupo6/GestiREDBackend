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


class ResourceTypeResource(ModelResource):
    class Meta:
        queryset = ResourceType.objects.all()
        resource_name = 'resourceType'
        authorization = Authorization()

class PhaseTypeResource(ModelResource):
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
    phaseType= fields.ForeignKey(PhaseTypeResource, 'phaseType', null=True, full=True)
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
    responsible  = fields.CharField(attribute="responsible")
    resource = fields.CharField(attribute="resource")
    class Meta:
        queryset = QualityControl.objects.all()
        resource_name = 'qualityControl'
        authorization = Authorization()


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