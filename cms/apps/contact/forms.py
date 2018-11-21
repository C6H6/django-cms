from django.forms import ModelForm
from cms.apps.contact.models import Inquiry


class InquiryForm(ModelForm):
    class Meta:
        model = Inquiry
        fields = ['name', 'email', 'text']
