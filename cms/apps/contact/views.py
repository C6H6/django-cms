from django.forms import ModelForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils import timezone
from django.contrib import messages

from cms.apps.contact.forms import InquiryForm


def index(request):
    form = InquiryForm()
    if request.user.is_authenticated:
        form.fields['name'].initial = request.user.username
        form.fields['email'].initial = request.user.email

    return render(request, 'contact/index.html', {'form': form})


def save(request):
    form = InquiryForm(request.POST)

    if form.is_valid():
        model = form.save(commit=False)  # type: ModelForm
        model.created_at = timezone.now()
        model.save()
        messages.add_message(request, messages.SUCCESS, 'Your message has been sent')

    return HttpResponseRedirect(reverse('contact:index'))
