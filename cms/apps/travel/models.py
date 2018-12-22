from django.db import models


class Travel(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    active = models.BooleanField(default=True)
    promotion_on_homepage = models.BooleanField(default=False)

    def __str__(self):
        return self.title
