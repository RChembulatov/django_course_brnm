from django.db import models


class Category(models.Model):
    name = models.CharField("Название категории", max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField("Название продукта", max_length=100)
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    stock = models.IntegerField("Количество продуктов на складе", default=0)

    def __str__(self):
        return f"{self.name}-{self.price}-{self.stock}"


class Sport(models.Model):
    name = models.CharField("Название спорта", max_length=100)

    def __str__(self):
        return self.name


class Country(models.Model):
    country_name = models.CharField("Название страны", max_length=100)

    def __str__(self):
        return self.country_name


class City(models.Model):
    city_name = models.CharField("Название города", max_length=100)
    street_name = models.CharField("Название улицы", max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.city_name


class Author(models.Model):
    name = models.CharField("Название автора", max_length=200)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField("Название книги", max_length=200)
    description = models.CharField("Описание книги", max_length=200)
    authors = models.ManyToManyField(Author)

    def __str__(self):
        return self.title


class Item(models.Model):
    name = models.CharField("Название для пагинации", max_length=100)
    description = models.CharField("Описание для пагинации", max_length=200)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField('Имя', max_length=100)
    email = models.EmailField('Email')
    message = models.TextField('Сообщение')
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)

    def __str__(self):
        return f'{self.name}-{self.email}'
