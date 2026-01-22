from django.db import models
from django.core.validators import MinValueValidator

class User(models.Model):
    name = models.CharField(max_length=100)

    # THIS LINE is the magic fix:
    def __str__(self):
        return self.name 

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    # THIS LINE fixes the product name:
    def __str__(self):
        return self.name

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(validators=[MinValueValidator(1)])