from django.db import models


class Restaurant(models.Model):
    name = models.CharField('Nom', max_length=100)
    email = models.EmailField(max_length=150, null=True)
    adresse = models.CharField(max_length=200)
    codePostal = models.BigIntegerField()
    ville = models.CharField(max_length=200, default="Mulhouse")
    phone = models.CharField('téléphone', max_length=12)
    website = models.URLField('site web')
    available = models.BooleanField('disponnible', default=True)
    picture = models.URLField('photo')

    def __str__(self):
        return self.name
