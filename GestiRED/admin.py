from django.contrib import admin
from .models import Privilege, Rol, User, TipoRecurso, Resource, ControlCalidad, TipoFase, Fase, Project, Evento, TipoEvento

# Register your models here.

admin.site.register(Privilege)
admin.site.register(Rol)
admin.site.register(User)
admin.site.register(TipoRecurso)
admin.site.register(Resource)
admin.site.register(ControlCalidad)
admin.site.register(TipoFase)
admin.site.register(Fase)
admin.site.register(Project)
admin.site.register(Evento)
admin.site.register(TipoEvento)
