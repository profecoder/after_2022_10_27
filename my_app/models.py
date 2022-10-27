from django.db import models

class Car(models.Model):
    brand = models.CharField(max_length=20)
    model = models.IntegerField()

    def __str__(self):
        return f"{self.brand} | {self.model}"


class House(models.Model):
    owner = models.CharField(max_length=30)
    address = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.owner} | {self.address}"
