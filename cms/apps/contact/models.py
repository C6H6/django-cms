from django.db import models


class Inquiry(models.Model):
    date = models.DateTimeField()
    name = models.CharField(max_length=30)
    email = models.EmailField()
    text = models.TextField(max_length=2000)
