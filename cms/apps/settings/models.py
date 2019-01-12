from django.db import models
from django.db.models import ImageField


class Settings(models.Model):
    site_logo = ImageField(upload_to='logo/', null=True)
    page_title = models.CharField(max_length=200)
    homepage_text = models.TextField()
    footer_text = models.TextField()
    left_column_text = models.TextField()
    mourning_mode = models.BooleanField(default=False)

    def __str__(self):
        return 'All settings'
