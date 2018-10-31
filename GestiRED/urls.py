from django.urls import path, include

from . import views
from .resources import *

user_resource = UserResource()
rol_resource = RolResource()
privilege_resource = PrivilegeResource()
resource_type_resource = ResourceTypeResource()
resource_resource = ResourceResource()
quality_control_resource = QualityControlResource()
phase_type_resource = PhaseTypeResource()
phase_resource = PhaseResource()
project_resource = ProjectResource()
event_type_resource = EventTypeResource()
event_resource = EventResource()
phase2_resource = Phase2Resource()

urlpatterns = [

    path('', include(user_resource.urls)),
    path('', include(rol_resource.urls)),
    path('', include(privilege_resource.urls)),
    path('', include(resource_type_resource.urls)),
    path('', include(resource_resource.urls)),
    path('', include(quality_control_resource.urls)),
    path('', include(phase_type_resource.urls)),
    path('', include(phase_resource.urls)),
    path('', include(phase2_resource.urls)),
    path('', include(project_resource.urls)),
    path('', include(event_type_resource.urls)),
    path('', include(event_resource.urls)),
    path('quality_review_notification/', views.quality_review_notification, name="send notification"),

]