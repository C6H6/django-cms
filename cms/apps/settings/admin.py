from django.contrib import admin

from cms.apps.settings.models import Settings


class AdminSettings(admin.ModelAdmin):
    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Settings, AdminSettings)
