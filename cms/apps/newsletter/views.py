from django.contrib import messages
from django.forms import ModelForm
from django.shortcuts import redirect

from cms.apps.newsletter.forms import NewsletterForm
from django.utils import timezone


def save_email(request):
    form = NewsletterForm(request.POST)

    if form.is_valid():
        model = form.save(commit=False)  # type: ModelForm
        model.created_at = timezone.now()
        model.active = True
        model.save()

        messages.add_message(request, messages.SUCCESS, 'Email saved successfully!', extra_tags="newsletter")

    next_url = request.POST.get('next', '/')
    return redirect(next_url)
