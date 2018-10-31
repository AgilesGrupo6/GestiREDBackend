from unittest import TestCase
import django
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "GestiREDBackend.settings")
django.setup()
from tastypie.test import ResourceTestCaseMixin



class TestQualityControlResource(ResourceTestCaseMixin,TestCase):

    def test_get_user_rols(self):
        resp = self.api_client.get('/gestired/user/?rols_in=2,3', format='json')
        self.assertValidJSONResponse(resp)
