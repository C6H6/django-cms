class CheckoutOffer(object):
    offer_id = 0

    def __init__(self, offer_id):
        self.offer_id = offer_id

    def serialize(self):
        return self.__dict__


class CheckoutSummary:
    total_price = 0
    offers = []
