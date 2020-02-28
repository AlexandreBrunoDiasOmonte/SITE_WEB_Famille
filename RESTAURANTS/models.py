from django.db import models
import re


class Restaurants(models.Model):
    name = models.CharField(max_length=100)
    adress = models.CharField(max_length=200)
    phone = models.CharField(max_length=10)
    website = models.URLField()

    def __str__(self):
        return {self.name, self.adress, self.phone, self.website}
