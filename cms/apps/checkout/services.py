from cms.apps.checkout.models import Purchase
from cms.apps.travel.models import Travel
from django.core.mail import send_mail


def process_purchase(offers, data, user):
    for offer in offers:
        new_purchase = Purchase()
        new_purchase.travel = Travel.objects.get(pk=offer.offer_id)
        new_purchase.user = user
        new_purchase.customer_first_name = data['first_name']
        new_purchase.customer_last_name = data['last_name']
        new_purchase.customer_address = data['address']
        new_purchase.customer_city = data['city']
        new_purchase.customer_phone = data['phone_number']
        new_purchase.passengers = offer.people
        new_purchase.passengers_data = ''
        new_purchase.save()

    return True


def send_purchase_mail(user, offers):
    bought_offers = ""
    for offer in offers:
        travel = Travel.objects.get(pk=offer.offer_id)
        bought_offers += travel.title + " (" + str(offer.people) + "),"
    bought_offers = bought_offers[:-1]

    text = "Thank You for purchase!\n- Details: " + bought_offers + " \n"

    send_mail("Thank you for purchase", text, "admin@django-cms.com", [user.email])

    return True
