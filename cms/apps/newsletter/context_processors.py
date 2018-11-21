from django.urls import reverse

from cms.apps.newsletter.forms import NewsletterForm


def newsletter_form(request):
    return {
        'newsletter_form': NewsletterForm(),
        'newsletter_form_url': reverse('newsletter:save_email')
    }
