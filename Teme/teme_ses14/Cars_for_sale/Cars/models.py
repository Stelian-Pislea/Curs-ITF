from django.db import models

CAR_MODELS = [
    ("S", "Sport"),
    ("J", "Jeep"),
    ("V", "Van")
]
FUEL = [
    ("diesel", "Diesel"),
    ("electric", "Electric"),
    ("gasoline", "Gasoline")
]


# Create your models here.
class Car(models.Model):
    name = models.CharField(max_length=50)
    year = models.CharField(max_length=30)
    model = models.CharField(max_length=1, choices=CAR_MODELS, null=False)
    fuel = models.CharField(max_length=8, choices=FUEL)

    def __str__(self):
        return f"{self.name} >>> {self.year} >>> {self.model} >>> {self.fuel}"
