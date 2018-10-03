from django.urls import path, include

from . import views
from .resources import *

user_resource = UserResource()
rol_resource = RolResource()
privilege_resource = PrivilegeResource()
perfil_resource = PerfilResource()
tipoRecurso_resource = TipoRecursoResource()
resource_resource = ResourceResource()
controlCalidad_resource = ControlCalidadResource()
tipoFase_resource = TipoFaseResource()
fase_resource = FaseResource()
project_resource = ProjectResource()

urlpatterns = [
    path('', views.index, name='index'),
    path('', include(user_resource.urls)),
    path('', include(rol_resource.urls)),
    path('', include(privilege_resource.urls)),
    path('', include(perfil_resource.urls)),
    path('', include(tipoRecurso_resource.urls)),
    path('', include(resource_resource.urls)),
    path('', include(controlCalidad_resource.urls)),
    path('', include(tipoFase_resource.urls)),
    path('', include(fase_resource.urls)),
    path('', include(project_resource.urls)),
]