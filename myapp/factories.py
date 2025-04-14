import factory
from factory.django import DjangoModelFactory
from myapp.models import Country, City, Author, Book


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


class AuthorFactory(DjangoModelFactory):
    class Meta:
        model = Author

    name = factory.Faker('name')


class BookFactory(DjangoModelFactory):
    class Meta:
        model = Book

    title = factory.Faker('sentence')
    description = factory.Faker('sentences', nb=3)

    @factory.post_generation
    def authors(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for author in extracted:
                self.authors.add(author)
