import factory
from factory.django import DjangoModelFactory
from myapp.models import Country, City


class CountryFactory(DjangoModelFactory):
    class Meta:
        model = Country

    country_name = factory.Faker('country')


class CityFactory(DjangoModelFactory):
    class Meta:
        model = City

    city_name = factory.Faker('city')
    street_name = factory.Faker('street_name')
    country = factory.SubFactory(CountryFactory)
