from django.db import models
from django.conf import settings


class Grooming(models.Model):

    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)


class Boarding(models.Model):

    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
