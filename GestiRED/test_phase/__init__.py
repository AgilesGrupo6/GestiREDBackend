from unittest import TestCase

from .models import Phase

class TestPhase(TestCase):
    def test_changePhase(self):
        self.assertEquals(Phase.changePhase("1,3"),"4","ActualPhase")
