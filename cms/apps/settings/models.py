from django.db import models
from django.db.models import ImageField


class Settings(models.Model):
        site_logo = ImageField(upload_to='logo/', null=True)
