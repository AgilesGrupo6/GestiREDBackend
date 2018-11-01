from unittest import TestCase
import django
import os
from django.conf import settings
from django.utils import timezone
from random import randrange
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'GestiREDBackend.settings')
django.setup()
from tastypie.test import ResourceTestCaseMixin

class test_qualityControl(ResourceTestCaseMixin,TestCase):
    def test_save(self):
        data={
            "observation": "Control Dibujo Kanban",
            "resource": "/gestired/resource/1/",
            "responsible": "/gestired/user/3/",
            "createUser": "/gestired/user/2/"
        }
        resp = self.api_client.post('/gestired/qualityControl/', format='json', data=data)
        self.assertHttpCreated(resp)