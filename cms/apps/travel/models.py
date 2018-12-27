from datetime import timedelta

from django.db import models
from django.utils import timezone
from django_countries.fields import CountryField


class Travel(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    active = models.BooleanField(default=True)
    country = CountryField()
    start_date = models.DateTimeField(default=(timezone.now() + timedelta(7)))
    end_date = models.DateTimeField(default=(timezone.now() + timedelta(14)))
    promotion_on_homepage = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class TravelImage(models.Model):
    travel = models.ForeignKey(Travel, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField()
