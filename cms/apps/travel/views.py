from django.shortcuts import render, get_object_or_404

from cms.apps.travel.models import Travel


def details(request, travel_id):
    travel = get_object_or_404(Travel, pk=travel_id, active=True)
    return render(request, 'travel/details.html', {'travel': travel})
