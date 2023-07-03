from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
class Coffee(models.Model):
    TEMP_TYPES = (
        ('hot', 'hot'),
        ('cold', 'cold')
    )
    COFFEE_TYPES = (
        ('LATTE', "LATTE"),
        ('AMERICANO', 'AMERICANO'),
        ('CAPPUCCINO', 'CAPPUCCINO'),
        ('BLACK', 'BLACK'),
    )
    coffee_type = models.CharField(choices=COFFEE_TYPES, max_length=50)
    sugar = models.IntegerField(default=50, validators=[MaxValueValidator(100), MinValueValidator(0)])
    price = models.DecimalField(max_digits=5, decimal_places=2)
    cold_hot = models.CharField(choices=TEMP_TYPES, max_length=40)

    def __str__(self):
        return f'{self.coffee_type}/{self.price}$/{self.cold_hot}/{self.sugar}%'
