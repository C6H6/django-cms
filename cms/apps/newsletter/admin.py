from django.contrib import admin
from cms.apps.newsletter.models import Newsletter
from cms.apps.newsletter.services import send_newsletter_mails


class NewsletterAdmin(admin.ModelAdmin):

    def get_fields(self, request, obj=None):
        fields = ['title', 'text']
        if obj:
            fields.append('created_at')
        return fields

    def save_model(self, request, obj, form, change):
        send_newsletter_mails(obj.title, obj.text)
        super(NewsletterAdmin, self).save_model(request, obj, form, change)

    def has_change_permission(self, request, obj=None):
        return False


admin.site.register(Newsletter, NewsletterAdmin)
