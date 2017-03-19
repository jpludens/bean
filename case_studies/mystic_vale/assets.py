from enum import Enum
from functools import total_ordering
from collections import Counter

# class ResourceCollection(Counter):  # what can this provide beyond a simple Counter?
#     @classmethod
#     def fromkeys(cls, iterable, v=None):
#         pass


# These are "units", "resources", "costs", or something...
class Spirit(Enum):
    __order__ = 'Sky Leaf Beast Wild Any'

    Sky = 1
    Leaf = 2
    Beast = 3
    Wild = 4
    Any = 5

    def __lt__(self, other):
        return self._value_ < (other._value_)


# These are "cards" with "costs"
class ValeCard(object):   # make this an abc?
    pass


# Level I Vale Cards
class AzureLake(ValeCard):
    name = "Azure Lake"
    level = 1
    cost = Counter([Spirit.Leaf, Spirit.Beast])


class BloomingArbor(ValeCard):
    name = "Blooming Arbor"
    level = 1
    cost = Counter([Spirit.Sky, Spirit.Leaf])


class CascadingFalls(ValeCard):
    name = "Cascading Falls"
    level = 1
    cost = Counter([Spirit.Beast, Spirit.Beast])


class ExodusRoad(ValeCard):
    name = "Exodus Road"
    level = 1
    cost = Counter([Spirit.Beast, Spirit.Sky])


class LeyLineNexus(ValeCard):
    name = "Ley Line Nexus"
    level = 1
    cost = Counter([Spirit.Sky, Spirit.Leaf])


class RadiantPinnacle(ValeCard):
    name = "Radiant Pinnacle"
    level = 1
    cost = Counter([Spirit.Sky, Spirit.Sky])


class SunstoneAerie(ValeCard):
    name = "Sunstone Aerie"
    level = 1
    cost = Counter([Spirit.Beast, Spirit.Sky])


class TalonthornDen(ValeCard):
    name = "Talonthorn Den"
    level = 1
    cost = Counter([Spirit.Leaf, Spirit.Leaf])


class WorldTree(ValeCard):
    name = "World Tree"
    level = 1
    cost = Counter([Spirit.Leaf, Spirit.Beast])


# Level II Vale Cards
class AncientLiferoots(ValeCard):
    name = "Ancient Liferoots"
    level = 2
    cost = Counter([Spirit.Sky, Spirit.Leaf, Spirit.Leaf, Spirit.Leaf])


class BlessedSavanna(ValeCard):
    name = "Blessed Savanna"
    level = 2
    cost = Counter([Spirit.Beast, Spirit.Beast, Spirit.Beast, Spirit.Beast])


class ConclaveOfEnts(ValeCard):
    name = "Conclave of Ents"
    level = 2
    cost = Counter([Spirit.Any, Spirit.Leaf, Spirit.Sky, Spirit.Beast])


class FeralGrove(ValeCard):
    name = "Feral Grove"
    level = 2
    cost = Counter([Spirit.Any, Spirit.Leaf, Spirit.Sky, Spirit.Beast])


class FungalForest(ValeCard):
    name = "Fungal Forest"
    level = 2
    cost = Counter([Spirit.Leaf, Spirit.Sky, Spirit.Sky])


class HeartwoodSanctuary(ValeCard):
    name = "Heartwood Sanctuary"
    level = 2
    cost = Counter([Spirit.Beast, Spirit.Leaf, Spirit.Leaf])


class PoolOfLight(ValeCard):
    name = "Pool of Light"
    level = 2
    cost = Counter([Spirit.Beast, Spirit.Sky, Spirit.Sky])


class ShimmeringBrook(ValeCard):
    name = "Shimmering Brook"
    level = 2
    cost = Counter([Spirit.Sky, Spirit.Sky, Spirit.Sky, Spirit.Sky])


class Skyhaven(ValeCard):
    name = "Skyhaven"
    level = 2
    cost = Counter([Spirit.Sky, Spirit.Beast, Spirit.Beast])


class StreamOfVigor(ValeCard):
    name = "Stream of Vigor"
    level = 2
    cost = Counter([Spirit.Leaf, Spirit.Beast, Spirit.Beast])


class VerdantValley(ValeCard):
    name = "Verdant Valley"
    level = 2
    cost = Counter([Spirit.Beast, Spirit.Beast, Spirit.Beast, Spirit.Sky, Spirit.Leaf])


class WebwoodCanopy(ValeCard):
    name = "Webwood Canopy"
    level = 2
    cost = Counter([Spirit.Leaf, Spirit.Leaf, Spirit.Leaf, Spirit.Leaf])


class WellspringGlade(ValeCard):
    name = "Wellspring Glade"
    level = 2
    cost = Counter([Spirit.Leaf, Spirit.Leaf, Spirit.Sky, Spirit.Sky, Spirit.Beast, Spirit.Beast])
