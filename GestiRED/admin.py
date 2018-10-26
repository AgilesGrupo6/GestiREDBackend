from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Privilege)
admin.site.register(Rol)
admin.site.register(User)
admin.site.register(ResourceType)
admin.site.register(Resource)
admin.site.register(QualityControl)
admin.site.register(PhaseType)
admin.site.register(Phase)
admin.site.register(Project)
admin.site.register(Event)
admin.site.register(EventType)
