from django.db import models


class Restaurant(models.Model):
    name = models.CharField('Nom', max_length=100, blank=False)
    email = models.EmailField(max_length=150, blank=True)
    adresse = models.CharField(max_length=200, blank=False)
    codePostal = models.BigIntegerField(default=68100, blank=False)
    ville = models.CharField(max_length=200, default="Mulhouse", blank=False)
    phone = models.CharField('téléphone', max_length=15, blank=True)
    website = models.URLField('site web', blank=True)
    available = models.BooleanField('disponnible', default=True)
    image = models.URLField("image", blank=True)

    def __str__(self):
        return self.name
