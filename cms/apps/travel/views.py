from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from cms.apps.checkout.models import Purchase
from cms.apps.travel.models import Travel
from django.db.models import Max, Min, Sum


def index(request):
    get = request.GET
    params = get_params(get)
    price_range = {'max': Travel.objects.all().aggregate(Max('price')),
                   'min': Travel.objects.all().aggregate(Min('price'))}
    all_travels = Travel.objects.filter(**params)
    page = get.get('p')
    paginator = Paginator(all_travels, 10)
    travels = paginator.get_page(page)
    return render(request, 'travel/index.html', {'travels': travels, 'params': params, 'price_range': price_range})


def details(request, travel_id):
    travel = get_object_or_404(Travel, pk=travel_id, active=True)
    places_taken = Purchase.objects.filter(travel=travel).aggregate(Sum('passengers'))
    places_left = travel.passengers_limit - (places_taken['passengers__sum'] or 0)
    return render(request, 'travel/details.html', {'travel': travel, 'places_left': places_left})


def get_params(params):
    result = {'active': True}
    if params.get('name'):
        result['title__contains'] = params.get('name')
    if params.get('country'):
        result['country'] = params.get('country')
    if params.get('price'):
        result['price__range'] = params.getlist('price')

    return result
