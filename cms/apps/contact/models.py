from django.db import models
from django.utils import timezone


class Inquiry(models.Model):
    created_at = models.DateTimeField()
    name = models.CharField(max_length=30)
    email = models.EmailField()
    text = models.TextField(max_length=2000)
    answer = models.TextField(max_length=2000, null=True)
    updated_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.created_at.__format__('%Y-%m-%d %H:%M:%S') + " | " + self.email + " | " + self.text[:100]

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.updated_at = timezone.now()
        super(Inquiry, self).save()
