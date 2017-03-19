from itertools import product
from collections import Counter


class Expander(object):
    def __init__(self, mapper):
        self.mapper = mapper

        self.payment_pool_cache = {}
        self.cost_pool_cache = {}

    def expand_payment_collection(self, collection):
        cache_key = tuple(sorted(collection.items()))
        try:
            return self.payment_pool_cache[cache_key]
        except KeyError:
            mappings = [self.mapper.map_unit_out(unit) for unit in collection.elements()]
            result = [Counter(prod) for prod in product(*mappings)]
            self.payment_pool_cache[cache_key] = result
            return result

    def expand_cost_collection(self, collection):
        cache_key = tuple(sorted(collection.items()))
        try:
            return self.cost_pool_cache[cache_key]
        except KeyError:
            mappings = [self.mapper.map_unit_in(unit) for unit in collection.elements()]
            result = [Counter(prod) for prod in product(*mappings)]
            self.cost_pool_cache[cache_key] = result
            return result
