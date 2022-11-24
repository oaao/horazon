"""Default item label restylings.

IMPORTANT: Item names are rendered bottom-up, for both composed and self-complete item names!
---------------------------------------------------------------------------------------------
e.g. 1) if you wanted 'PICK ME' *above* an item name, you would "\n  {name}  \n  PICK ME  \n"
e.g. 2) A colour tag *terminating* an item name will apply to the row above it.
      - "{_.ORANGE}Diadem" would mean "Griffon's Eye" shows above it in unique colour.
      - "{_.ORANGE}Diadem{_.WHITE}" would mean "Griffon's Eye" becomes white!
"""
from ..styling import colours as _


# Many label restyles copy from or iterate on (with permission) AlexisEvo's original work
# https://github.com/AlexisEvo/d2r-loot-filter
ITEMS = (
    {
        # key — removed by default, but styled since it can smooth out LK run pit stops
        "key": "key",
        "long_name": f"{_.GREY}[{_.GOLD}k{_.GREY}]",
        "short_name": f"{_.GREY}[ {_.GOLD}k{_.GREY} ]",
    },
    # ------------------------------------------------ regen potions
    {
        # super healing potion
        "key": "hp5",
        "long_name": f"{_.RED}health{_.WHITE}POT",
        "short_name": f"{_.RED}h{_.WHITE}POT",
    },
    {
        # super mana potion
        "key": "mp5",
        "long_name": f"{_.BLUE}mana{_.WHITE}POT",
        "short_name": f"{_.BLUE}m{_.WHITE}POT",
    },
    {
        # rejuvenation potion
        "key": "rvs",
        "long_name": f"{_.PURPLE}35{_.WHITE}juv",
        "short_name": f"{_.PURPLE}35{_.WHITE}j",
    },
    {
        # rejuvenation potion
        "key": "rvl",
        "long_name": f"{_.PURPLE}FULL{_.WHITE}juv",
        "short_name": f"{_.PURPLE}FULL{_.WHITE}j",
    },
    # ------------------------------------------------ scrolls & tomes
    {
        # scroll of town portal
        "key": "tsc",
        "long_name": f"{_.BLUE}§{_.WHITE}tp",
        "short_name": f"{_.BLUE}§",
    },
    {
        # tome of town portal
        "key": "tbk",
        "long_name": f"{_.BLUE}§{_.WHITE}tome",
        "short_name": f"{_.BLUE}§{_.WHITE}[]",
    },
    {
        # scroll of identify
        "key": "isc",
        "long_name": f"{_.RED}§{_.WHITE}id",
        "short_name": f"{_.RED}§",
    },
    {
        # tome of identify
        "key": "ibk",
        "long_name": f"{_.RED}§{_.WHITE}tome",
        "short_name": f"{_.RED}§{_.WHITE}[]",
    },
    # ------------------------------------------------ gems (flawless & perfect)
    # TODO: all flawless and perfect gems (i don't like any of my current stylings)
    # ------------------------------------------------ charms (small & grand)
    # TODO: small & grand charms (i don't like my current stylings)
)


AFFIXES = (
    {
        # gold
        "key": "glg",
        "long_name": f"{_.GOLD}g",
        "short_name": f"{_.GOLD}g",
    },
)
