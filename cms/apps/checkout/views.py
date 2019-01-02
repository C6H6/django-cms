from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import datetime

from cms.apps.checkout.classes import CheckoutOffer, CheckoutSummary
from cms.apps.travel.models import Travel


@login_required(login_url='/login/')
def add(request):
    data = request.POST
    count = int(data.get('count') or 1)
    offer = CheckoutOffer(data.get('travel-id'), count)
    existing = request.session.get('offers', [])

    for exist in existing:
        if offer.offer_id == exist.offer_id:
            return render(request, 'checkout/offer_exists.html')

    existing.append(offer)
    request.session['offers'] = existing
    return redirect('checkout:new')


@login_required(login_url='/login/')
def new(request):
    return render(request, 'checkout/new.html')


@login_required(login_url='/login/')
def summary(request):
    offers = request.session.get('offers')

    if not offers:
        return redirect('travel:index')

    checkout_summary = CheckoutSummary
    checkout_summary.offers = []

    total = 0

    for checkout_offer in offers:
        count = int(checkout_offer.people)
        offer = Travel.objects.get(pk=checkout_offer.offer_id)
        total += offer.price * count
        checkout_summary.offers.append({'offer': offer, 'people': count, 'total': offer.price * count})

    checkout_summary.total_price = total

    now = datetime.datetime.now()
    years = range(now.year, now.year + 10)
    months = range(1, 12)

    return render(request, 'checkout/summary.html', {'summary': checkout_summary, 'years': years, 'months': months})


@login_required(login_url='/login/')
def remove(request, offer_id):
    existing = request.session.get('offers', [])

    for exist in existing:
        if int(exist.offer_id) == offer_id:
            existing.remove(exist)

    request.session['offers'] = existing
    return redirect('checkout:summary')
