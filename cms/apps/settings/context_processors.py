from cms.apps.settings.models import Settings


def settings_processor(request):
    settings = Settings.objects.all().first()
    return {'settings': settings}
