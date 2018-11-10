from django.forms import ModelForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils import timezone

from cms.apps.contact.forms import InquiryForm


def index(request):
    form = InquiryForm()
    return render(request, 'contact/index.html', {'form': form})


def save(request):
    form = InquiryForm(request.POST)

    if form.is_valid():
        model = form.save(commit=False)  # type: ModelForm
        model.created_at = timezone.now()
        model.save()

    return HttpResponseRedirect(reverse('contact:index'))
