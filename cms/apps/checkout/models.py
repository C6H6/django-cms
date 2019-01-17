from django.db import models
from django.contrib.auth import get_user_model

from cms.apps.travel.models import Travel


class Purchase(models.Model):
    travel = models.ForeignKey(Travel, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    customer_first_name = models.CharField(max_length=100)
    customer_last_name = models.CharField(max_length=100)
    customer_address = models.CharField(max_length=100)
    customer_city = models.CharField(max_length=50)
    customer_phone = models.CharField(max_length=15)
    passengers = models.IntegerField()
    passengers_data = models.TextField()

    def __str__(self):
        return self.travel.title + " | " + self.user.username + " | (" + str(self.passengers) + ")"
