from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from cms.apps.checkout.classes import CheckoutOffer, CheckoutSummary
from cms.apps.travel.models import Travel


@login_required(login_url='/login/')
def add(request):
    data = request.POST
    print(data.get('travel-id'))
    offer = CheckoutOffer(data.get('travel-id'))
    existing = request.session.get('offers', [])
    existing.append(offer)
    request.session['offers'] = existing
    return redirect('checkout:summary')


@login_required(login_url='/login/')
def summary(request):
    offers = request.session.get('offers')

    checkout_summary = CheckoutSummary
    total = 0

    for checkout_offer in offers:
        offer = Travel.objects.get(pk=checkout_offer.offer_id)
        total += offer.price * 1
        checkout_summary.offers.append({'offer': offer, 'people': 1, 'total': offer.price * 1})

    checkout_summary.total_price = total
    return render(request, 'checkout/summary.html', {'summary': checkout_summary})
