from django import forms
from django.forms import ModelForm
from cms.apps.contact.models import Inquiry
from django.forms.widgets import TextInput


class InquiryForm(ModelForm):
    name = forms.CharField(
        widget=TextInput(attrs={'class': 'form-control input-sm chat-input', 'placeholder': 'Name'}))

    email = forms.CharField(
        widget=TextInput(attrs={'class': 'form-control input-sm chat-input', 'placeholder': 'Email'}))

    text = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control input-sm chat-input', 'placeholder': ''}))

    class Meta:
        model = Inquiry
        fields = ['name', 'email', 'text']
