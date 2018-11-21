from django.forms import ModelForm
from cms.apps.newsletter.models import NewsletterEmail


class NewsletterForm(ModelForm):
    class Meta:
        model = NewsletterEmail
        fields = ['email']
