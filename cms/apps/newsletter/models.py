from django.db import models
from django.utils import timezone


class NewsletterEmail(models.Model):
    created_at = models.DateTimeField()
    email = models.EmailField()
    active = models.BooleanField(default=True)

    class Meta:
        db_table = 'newsletter_email'


class Newsletter(models.Model):
    created_at = models.DateTimeField()
    title = models.CharField(max_length=200)
    text = models.TextField()

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.created_at = timezone.now()
        super(Newsletter, self).save()

    def has_change_permission(self, request, obj=None):
        return False

    def __str__(self):
        return self.title + " (" + self.created_at.__format__('%Y-%m-%d') + ")"

    class Meta:
        db_table = 'newsletter'
