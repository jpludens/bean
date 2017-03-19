from itertools import product


class Mapper(object):
    def __init__(self):
        self._payments_to_costs = {}
        self._costs_to_payments = {}

    def map_unit_out(self, unit):
        return self._payments_to_costs[unit]

    def map_unit_in(self, unit):
        return self._costs_to_payments[unit]

    def add_link(self, pay, cost):
        if pay not in self._payments_to_costs:
            self._payments_to_costs[pay] = []
        self._payments_to_costs[pay].append(cost)

        if cost not in self._costs_to_payments:
            self._costs_to_payments[cost] = []
        self._costs_to_payments[cost].append(pay)

    def add_links(self, pays, costs):
        for pay, cost in product(pays, costs):
            self.add_link(pay, cost)

    def add_identities(self, *args):
        for unit in args:
            self.add_link(unit, unit)

    def add_pay_fulfillments(self, pay, costs):
        for cost in costs:
            self.add_link(pay, cost)

    def add_cost_fulfillments(self, pays, cost):
        for pay in pays:
            self.add_link(pay, cost)