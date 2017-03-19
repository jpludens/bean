# Is cost X satisfied by resources Y?
# What is left in the resource pool after satisfying cost?
# What additional resources are needed to satisfy cost?

from collections import Counter
from itertools import combinations


class Checker(object):
    @staticmethod
    def add_costs(buyables):
        return reduce(lambda acc, c: acc + c.cost, buyables, Counter())

    def __init__(self, mapper, expander):
        self.mapper = mapper
        self.expander = expander

    def pool_can_buy(self, pool, cost):
        pools = self.expander.expand_payment_collection(pool)
        costs = self.expander.expand_cost_collection(cost)
        return any([ccr.met
                    for ccr in [CostCheckResult(p, c)
                                for p in pools
                                for c in costs]])

    def prospects(self, pool, items, max_items=None):
        if max_items is None:
            max_items = len(items)

        item_sets = reduce(lambda acc, i: acc + [c for c in combinations(items, i + 1)], range(max_items), [])
        return [item_set for item_set in item_sets
                if self.pool_can_buy(pool, Checker.add_costs(item_set))]


class CostCheckResult(object):
    def __init__(self, pool, cost):
        self.pool = pool
        self.cost = cost

        self.left = pool - cost
        self.short = cost - pool
        self.met = not self.short

    # def then(self, cost):
    #     return SingleCostCheck(self.left, cost)
    #
    # def lend(self, lent):
    #     return SingleCostCheck(self.pool + lent, self.cost)


# class MultiCostCheck(object):
#     def __init__(self, pools, costs):
#         self.pools = pools
#         self.costs = costs
#
#         self.single_cost_checks = [SingleCostCheck(p, c)
#                                    for p in pools for c in costs]
#         self.met = any([scc.met for scc in self.single_cost_checks])

#
# def get_cost_checks(pool, buyables):
#     return {b: CostCheckResult(pool, b.cost) for b in buyables}

#
# def naive_single_purchase(pool, items):
#     return [item for item in items if CostCheckResult(pool, item.cost).met]

#
# def naive_double_purchase(pool, items):
#     affordable_items = [item for item in items
#                         if CostCheckResult(pool, item.cost).met]
#     affordable_pairs = [pair for pair in combinations(affordable_items, 2)
#                         if CostCheckResult(pool, pair[0].cost + pair[1].cost).met] # change to use add_costs
#     return [(item,) for item in affordable_items] + affordable_pairs


# def naive_multiple_purchases(pool, items, max_items=None):
#     if max_items is None:
#         max_items = len(items)
#
#     item_sets = reduce(lambda acc, i: acc + [c for c in combinations(items, i+1)], range(max_items), [])
#     return [item_set for item_set in item_sets
#             if CostCheckResult(pool, Checker.add_costs(item_set)).met]


# NEXT
# Need to handle cases where part of a cost can be fulfilled with various resources,
# or where a resource pool can provide different combinations of resources
# (for bonus points, handle the case of being allowed to convert/condense resources)


############### junk for playing around #################
class Buyable(object):
    def __init__(self, name, cost=None):
        self.name = name
        self.cost = Counter() if cost is None else cost

    def __str__(self):
        return self.name


Brickhouse = Buyable("Brickhouse", Counter(["clay"]))
Baths = Buyable("Baths", Counter(["stone"]))
Barracks = Buyable("Barracks", Counter(["wood"]))
Bar = Buyable("Bar", Counter(["ore"]))
Palace = Buyable("Palace",
                 Counter(["clay", "stone", "wood", "ore", "paper", "cloth", "glass"]))
Wall = Buyable("Wall",
               Counter(["ore", "ore", "ore"]))

buildings = [Brickhouse, Baths, Bar, Barracks, Palace, Wall]

player_a = Counter(["clay", "clay", "ore", "ore", "ore", "glass"])
player_b = Counter(["clay", "stone", "wood", "ore", "paper", "cloth", "glass"])
player_c = Counter(["ore", "ore"])

import pprint
pp = pprint.PrettyPrinter().pprint
