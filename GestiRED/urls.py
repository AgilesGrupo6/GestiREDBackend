from django.urls import path, include

from . import views
from .resources import *

user_resource = UserResource()
rol_resource = RolResource()
privilege_resource = PrivilegeResource()
tipoRecurso_resource = TipoRecursoResource()
resource_resource = ResourceResource()
controlCalidad_resource = ControlCalidadResource()
tipoFase_resource = TipoFaseResource()
fase_resource = FaseResource()
project_resource = ProjectResource()
tipo_evento_resource = TipoEventoResource()
evento_resource = EventoResource()

urlpatterns = [
    path('', views.index, name='index'),
    path('', include(user_resource.urls)),
    path('', include(rol_resource.urls)),
    path('', include(privilege_resource.urls)),
    path('', include(tipoRecurso_resource.urls)),
    path('', include(resource_resource.urls)),
    path('', include(controlCalidad_resource.urls)),
    path('', include(tipoFase_resource.urls)),
    path('', include(fase_resource.urls)),
    path('', include(project_resource.urls)),
    path('', include(tipo_evento_resource.urls)),
    path('', include(evento_resource.urls)),
]