class CheckoutOffer(object):
    offer_id = 0
    people = 0

    def __init__(self, offer_id, people):
        self.offer_id = offer_id
        self.people = people

    def serialize(self):
        return self.__dict__


class CheckoutSummary:
    total_price = 0
    offers = []
