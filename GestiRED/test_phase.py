from unittest import TestCase
import django
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "GestiREDBackend.settings")
django.setup()

from django.conf import settings
from GestiRED.models import Phase,Resource, PhaseType
from django.utils import timezone


class TestPhase(TestCase):

    def test_save_phase(self):
        resource=Resource.objects.filter(id=1)
        tf=PhaseType.objects.filter(id=4)

        phase= Phase(initDate=timezone.now(), resource=resource, phaseType=tf)
        phase.save()

        self.assertEqual(phase.phaseType.name, "Control de calidad")
