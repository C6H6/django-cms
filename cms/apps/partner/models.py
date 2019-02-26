from django.contrib.auth import get_user_model
from django.db import models

from cms.apps.checkout.models import Purchase


class Partner(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    code = models.CharField(max_length=10)


class PartnerPurchase(models.Model):
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE)
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE)
