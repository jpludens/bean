from bean.expander import Expander
from bean.mapper import Mapper
from bean.checker import Checker
from case_studies.mystic_vale.assets import *

# Links can be added individually
mapper = Mapper()
mapper.add_link(Spirit.Sky, Spirit.Sky)
mapper.add_link(Spirit.Leaf, Spirit.Leaf)
mapper.add_link(Spirit.Beast, Spirit.Beast)

mapper.add_link(Spirit.Wild, Spirit.Sky)
mapper.add_link(Spirit.Wild, Spirit.Leaf)
mapper.add_link(Spirit.Wild, Spirit.Beast)

mapper.add_link(Spirit.Sky, Spirit.Any)
mapper.add_link(Spirit.Leaf, Spirit.Any)
mapper.add_link(Spirit.Beast, Spirit.Any)

mapper.add_link(Spirit.Wild, Spirit.Any)

# print "\n\n\n"
# Links can be also added more economically
mapper2 = Mapper()
mapper2.add_identities(Spirit.Sky, Spirit.Leaf, Spirit.Beast)
mapper2.add_pay_fulfillments(Spirit.Wild, [Spirit.Sky, Spirit.Leaf, Spirit.Beast])
mapper2.add_cost_fulfillments([Spirit.Sky, Spirit.Leaf, Spirit.Beast], Spirit.Any)
mapper2.add_link(Spirit.Wild, Spirit.Any)

# print "Units mapped to costs they can fulfill"
# print mapper2._payments_to_costs
# print "Costs mapped to units that can fulfill them"
# print mapper2._costs_to_payments

expander = Expander(mapper2)
# print "\n\nExpansion of what Sky/Beast can pay for"
# print expander.expand_payment_unit([Spirit.Sky, Spirit.Beast])
#
# print "\n\nExpansion of hat can pay for Sky/Leaf/Beast/Any"
# import pprint
# pays = expander.expand_cost_unit([Spirit.Any, Spirit.Sky, Spirit.Leaf, Spirit.Beast])
# pprint.PrettyPrinter().pprint(pays)
# print "That's", len(pays), "ways to pay!"


checker = Checker(mapper2, expander)
vales = [
    AzureLake(), BloomingArbor(), SunstoneAerie(), TalonthornDen(),
    AncientLiferoots(), ConclaveOfEnts(), ShimmeringBrook(), PoolOfLight()
]

pool1 = Counter([Spirit.Sky, Spirit.Beast])
pool2 = Counter([Spirit.Sky, Spirit.Beast, Spirit.Wild])
pool3 = Counter([Spirit.Sky, Spirit.Leaf, Spirit.Wild, Spirit.Leaf])
pool4 = Counter([Spirit.Wild, Spirit.Wild, Spirit.Beast, Spirit.Sky, Spirit.Sky, Spirit.Beast])


# import cProfile
# cProfile.runctx('checker.prospects(pool4, vales, max_items=2)', globals(), locals())
