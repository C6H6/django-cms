from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import datetime
from django.utils.html import escape

from cms.apps.checkout.classes import CheckoutOffer, CheckoutSummary
from cms.apps.checkout.models import Purchase
from cms.apps.checkout.services import process_purchase
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


@login_required(login_url='/login/')
def purchase(request):
    data = request.POST
    offers = request.session.get('offers')
    user = request.user

    result = process_purchase(offers, data, user)

    if result:
        del request.session['offers']
        request.session.modified = True
        return render(request, 'checkout/purchase_completed.html')

    return HttpResponse(escape(repr(request)))