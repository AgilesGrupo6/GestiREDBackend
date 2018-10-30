from unittest import TestCase
import django
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "GestiREDBackend.settings")
django.setup()

from django.conf import settings
from GestiRED.models import Phase


class TestPhase(TestCase):

    def test_change_phase_resource(self):
        self.assertEqual(Phase.change_phase_resource(1, 2), "Phase.phaseType.name")
