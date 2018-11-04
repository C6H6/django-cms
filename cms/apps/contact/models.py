from django.db import models


class Inquiry(models.Model):
    date = models.DateTimeField()
    name = models.CharField(max_length=30)
    email = models.EmailField()
    text = models.TextField(max_length=2000)

    def __str__(self):
        return self.date.__format__('%Y-%m-%d %H:%M:%S') + " | " + self.email + " | " + self.text[:100]
