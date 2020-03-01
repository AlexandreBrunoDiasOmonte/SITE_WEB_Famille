from django.db import models
import re


class Restaurants(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=150, default="name@exemple.com")
    adresse = models.CharField(max_length=200)
    ville = models.CharField(max_length=200)
    phone = models.CharField(max_length=10)
    website = models.URLField()

    def __str__(self):
        return {self.name, self.email, self.phone, self.website}
