'''
from unittest import TestCase
import django
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "GestiREDBackend.settings")
django.setup()

from django.conf import settings
from .models import Phase,Resource, PhaseType
from django.utils import timezone
from random import randrange
from tastypie.test import ResourceTestCaseMixin


class TestPhase(ResourceTestCaseMixin,TestCase):
    #Se espera que solo quede un solo registro activo (sin valor en endDate)
    def test_save_phase(self):
        phase = Phase(initDate=timezone.now(), resource_id=1, phaseType_id=randrange(5)+1)
        phase.save()
        lst = Phase.objects.filter(resource__id=1, endDate=None)

        if len(lst) != 1:
            phase.delete()

        self.assertEqual(len(lst), 1)

    def test_get_resources_phase(self):
        resp = self.api_client.get('/gestired/resources/?phaseType=3', format='json')
        self.assertValidJSONResponse(resp)
'''