class CheckoutOffer(object):
    offer_id = 0
    people = 0
    ref = None

    def __init__(self, offer_id, people, ref):
        self.offer_id = offer_id
        self.people = people
        self.ref = ref

    def serialize(self):
        return self.__dict__


class CheckoutSummary:
    total_price = 0
    total_discount = 0
    offers = []
