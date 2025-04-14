from django.test import TestCase
from .models import Sport, Country, City, Book
from .factories import CountryFactory, CityFactory, AuthorFactory, BookFactory


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


class AuthorAndBookModelTest(TestCase):
    def test_author_and_book_creation(self):
        author = AuthorFactory(name="Толстой")
        book = BookFactory(title="Война и мир", description="Описание")

        self.assertEqual(author.name, "Толстой")
        self.assertEqual(book.title, "Война и мир")
        self.assertEqual(book.description, "Описание")

    def test_author_books_relationship(self):
        author = AuthorFactory(name="Достоевский")
        book1 = BookFactory(title="Преступление и наказание", authors=[author])
        book2 = BookFactory(title="Идиот", authors=[author])

        # Проверка, что 2 книги
        self.assertEqual(author.book_set.count(), 2)
        self.assertEqual(Book.objects.filter(authors=author).count(), 2)

        # Есть книги 1 и 2 у автора
        self.assertEqual(book1.authors.first().name, "Достоевский")
        self.assertEqual(book2.authors.first().name, "Достоевский")
