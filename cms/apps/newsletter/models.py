from django.db import models


class NewsletterEmail(models.Model):
    created_at = models.DateTimeField()
    email = models.EmailField()
    active = models.BooleanField(default=True)

    class Meta:
        db_table = 'newsletter_email'
