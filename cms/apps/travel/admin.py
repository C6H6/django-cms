from django.contrib import admin

from cms.apps.travel.models import Travel, TravelImage


class TravelImageInline(admin.TabularInline):
    model = TravelImage
    extra = 1


class TravelAdmin(admin.ModelAdmin):
    inlines = [TravelImageInline]

    readonly_fields = ['rejections']


admin.site.register(Travel, TravelAdmin)
