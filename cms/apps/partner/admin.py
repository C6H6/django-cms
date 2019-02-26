import random
import string

from django.contrib import admin

from cms.apps.partner.models import Partner


class PartnerAdmin(admin.ModelAdmin):

    def get_fields(self, request, obj=None):
        fields = ['user']
        if obj:
            fields.append('code')
        return fields

    def get_readonly_fields(self, request, obj=None):
        fields = ['code']
        if obj:
            fields.append('user')
        return fields

    def save_model(self, request, obj, form, change):
        if not obj.code:
            obj.code = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
        super(PartnerAdmin, self).save_model(request, obj, form, change)


admin.site.register(Partner, PartnerAdmin)
