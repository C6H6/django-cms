from django.db import models
from django.db.models import IntegerField
from django.utils import timezone
from django_countries.fields import CountryField


def default_start_date():
    return timezone.now() + timezone.timedelta(days=7)


def default_end_date():
    return timezone.now() + timezone.timedelta(days=14)


class Travel(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    active = models.BooleanField(default=True)
    country = CountryField()
    passengers_limit = IntegerField(default=20)
    start_date = models.DateTimeField(default=default_start_date)
    end_date = models.DateTimeField(default=default_end_date)
    promotion_on_homepage = models.BooleanField(default=False)
    rejections = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class TravelImage(models.Model):
    travel = models.ForeignKey(Travel, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField()
