from django.contrib import admin
from .models import Inquiry
from django.core.mail import send_mail


class InquiryAdmin(admin.ModelAdmin):
    fields = ['created_at', 'name', 'email', 'text', 'answer']

    def get_readonly_fields(self, request, obj=None):
        fields = ['created_at', 'name', 'email', 'text']
        if obj and obj.answer:
            fields.append('answer')
        return fields

    def has_add_permission(self, request):
        return False

    def save_model(self, request, obj, form, change):
        send_mail("Contact response", obj.answer, "admin@cms.com", [obj.email], False)
        super(InquiryAdmin, self).save_model(request, obj, form, change)


admin.site.register(Inquiry, InquiryAdmin)
