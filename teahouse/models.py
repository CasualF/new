from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Tea(models.Model):
    TEMP_TYPES = (
        ('hot', 'hot'),
        ('cold', 'cold')
    )
    TEA_TYPES = (
        ('GREEN', "GREEN"),
        ('BLACK', 'BLACK'),
        ('CREAM', 'CREAM'),
        ('OOLONG', 'OOLONG'),
    )
    tea_type = models.CharField(choices=TEA_TYPES, max_length=50)
    sugar = models.IntegerField(default=50, validators=[MaxValueValidator(100), MinValueValidator(0)])
    price = models.DecimalField(max_digits=5, decimal_places=2)
    cold_hot = models.CharField(choices=TEMP_TYPES, max_length=40)
    flavour = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f'{self.tea_type}/{self.price}$/{self.cold_hot}/{self.sugar}%/{self.flavour if self.flavour else "No flavour"}'
