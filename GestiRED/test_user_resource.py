from unittest import TestCase
import django
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "GestiREDBackend.settings")
django.setup()
from tastypie.test import ResourceTestCaseMixin


class TestUserResource(ResourceTestCaseMixin,TestCase):
    def test_save(self):
        self.fail()

    def test_get_user_resources(self):
        resp = self.api_client.get('/gestired/resourcesxuser/?user_in=2', format='json')
        self.assertTrue(len(self.deserialize(resp)['objects'])>0)
        #self.assertValidJSONResponse(resp)
