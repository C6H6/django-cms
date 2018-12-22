from django.shortcuts import render

from cms.apps.travel.models import Travel


def index(request):
    promoted = Travel.objects.filter(promotion_on_homepage=True, active=True)
    return render(request, 'core/index.html', {'promoted': promoted})
