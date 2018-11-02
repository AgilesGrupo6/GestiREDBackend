from django.db import models
from django.utils import timezone
import logging, logging.config
import sys
LOGGING = {
    'version': 1,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'stream': sys.stdout,
        }
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO'
    }
}

logging.config.dictConfig(LOGGING)
class Privilege(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return '%s' % self.name


class Rol(models.Model):
    name = models.CharField(max_length=200)
    privileges = models.ManyToManyField(Privilege)

    def __str__(self):
        return '%s' % self.name


class User(models.Model):
        name = models.CharField(max_length=200)
        surname = models.CharField(max_length=200)
        email = models.CharField(max_length=200)
        password = models.CharField(max_length=200)
        registrationDate = models.DateTimeField(default=timezone.now)
        rols =  models.ManyToManyField(Rol)

        def __str__(self):
            return '%s %s' % (self.name, self.surname)


class ResourceType(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return '%s' % self.name


class Resource(models.Model):
    name = models.CharField(max_length=200)
    labels = models.CharField(max_length=2000)
    registrationDate = models.DateTimeField(default=timezone.now)
    url = models.CharField(max_length=200)
    resourceType = models.ForeignKey(ResourceType, on_delete=models.CASCADE)
    responsibles = models.ManyToManyField('User')
    #fases = models.ForeignKey('Fase', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if self.id is None or self.name not in self.labels:
            self.labels = self.name + ' ' + self.labels
        super().save(*args, **kwargs)  # Call the "real" save() method.

    def __str__(self):
        return '%s' % self.name

class QualityControl(models.Model):
    observation = models.CharField(max_length=200)
    responsible = models.ForeignKey(User, on_delete=models.CASCADE,related_name='assign_user')
    createUser = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='create_user')
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    state = models.CharField(max_length=1, default='A', null=True, blank=True)


class PhaseType(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return '%s' % self.name


class Phase(models.Model):
    initDate = models.DateTimeField(default=timezone.now)
    endDate = models.DateTimeField(null=True, blank=True)
    phaseType = models.ForeignKey(PhaseType, on_delete=models.CASCADE)
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)

    def __str__(self):
        return  self.resource.name  +' - '+ self.phaseType.name

    def save(self, *args, **kwargs):
        logging.info("----->phases")
        phase_qc = -1
        ph = Phase.objects.filter(resource__id=self.resource.id, endDate=None)
        ph_size = len(ph)

        if ph_size > 0:
            phase_qc = ph[0].phaseType.id

        ph.update(endDate=timezone.now())

        if ph_size == 1 and phase_qc == 4:
           qc= QualityControl.objects.filter(resource__id=self.resource.id)
           qc.update(state='C')
        super().save(*args, **kwargs)  # Call the "real" save() method.


class Project(models.Model):
    name = models.CharField(max_length=200)
    labels = models.CharField(max_length=2000)
    registrationDate = models.DateTimeField(default=timezone.now)
    resources = models.ManyToManyField(Resource)

    def save(self, *args, **kwargs):
        if self.id is None or self.name not in self.labels:
            self.labels = self.name + ' ' + self.labels
        super().save(*args, **kwargs)  # Call the "real" save() method.

    def __str__(self):
        return '%s' % self.name


class EventType(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return '%s' % self.name


class Event(models.Model):
    initDate = models.DateTimeField(default=timezone.now)
    eventType = models.ForeignKey(EventType, on_delete=models.CASCADE)
    description = models.CharField(max_length=500, null=True, blank=True)
    user = models.ForeignKey(User, default='1', on_delete=models.CASCADE)
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    artifact = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return  self.resource.name  +' - '+ self.eventType.name


class Comments(models.Model):
    date = models.DateTimeField(default=timezone.now)
    value = models.CharField(max_length=500, null=True, blank=True)
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    #qualityControl = models.ForeignKey(QualityControl, on_delete=models.CASCADE)

    def __str__(self):
        return  self.value