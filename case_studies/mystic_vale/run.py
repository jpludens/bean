from case_studies.mystic_vale.study import *

sky = Spirit.Sky
leaf = Spirit.Leaf
beast = Spirit.Beast
wild = Spirit.Wild
ne = Spirit.Any

ba = BloomingArbor
al = AncientLiferoots
lln = LeyLineNexus
er = ExodusRoad
cf = CascadingFalls
sa = SunstoneAerie
az = AzureLake
wt = WorldTree
rp = RadiantPinnacle
td = TalonthornDen
wc = WebwoodCanopy
pl = PoolOfLight
sv = StreamOfVigor
ff = FungalForest
bs = BlessedSavanna
sh = Skyhaven
fg = FeralGrove
hs = HeartwoodSanctuary
vv = VerdantValley
wg = WellspringGlade
ce = ConclaveOfEnts
sb = ShimmeringBrook

vales = []


def add_vale(vale):
    vales.append(vale)


def remove_vale(vale):
    vales.remove(vale)


def clear_vales():
    global vales
    vales = vales[:]


def view_vales():
    for v in vales:
        print v.name


def what_vales(*spirits):
    checker_results = checker.prospects(Counter(spirits), vales, max_items=2)
    for r in checker_results:
        print [v.name for v in r]
