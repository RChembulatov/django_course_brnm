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
