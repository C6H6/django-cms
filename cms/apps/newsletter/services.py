from django.core.mail import send_mail

from cms.apps.newsletter.models import NewsletterEmail


def send_newsletter_mails(title, text):
    mails = NewsletterEmail.objects.filter(active=1)

    for mail in mails:
        send_mail(title, text, "newsletter@cms.com", [mail.email])
