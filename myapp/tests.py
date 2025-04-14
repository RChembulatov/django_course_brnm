from django.test import TestCase
from .models import Sport


class SportModelTest(TestCase):
    def setUp(self):
        self.football = Sport.objects.create(name="Football")

    def test_football_name(self):
        self.assertEqual(self.football.name, "Football")
