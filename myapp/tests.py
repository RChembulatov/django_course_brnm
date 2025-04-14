from django.test import TestCase
from .models import Sport, Country, City
from .factories import CountryFactory, CityFactory


class SportModelTest(TestCase):
    def setUp(self):
        self.football = Sport.objects.create(name="Football")

    def test_football_name(self):
        self.assertEqual(self.football.name, "Football")


# Через фикстуру
class CountryFixturesTest(TestCase):
    fixtures = ['country.json']

    def test_country(self):
        italy = Country.objects.get(country_name="Italy")
        france = Country.objects.get(country_name="France")
        self.assertEqual(italy.country_name, "Italy")
        self.assertEqual(france.country_name, "France")


# Через фабрику
class CityFactoryTest(TestCase):
    def test_city(self):
        country = CountryFactory(country_name="Italy")

        city = CityFactory(
            city_name="Rome",
            street_name="Via del Corso",
            country=country
        )

        self.assertEqual(city.city_name, "Rome")
        self.assertEqual(city.street_name, "Via del Corso")
        self.assertEqual(city.country.country_name, "Italy")
        self.assertIsInstance(city.country, Country)
