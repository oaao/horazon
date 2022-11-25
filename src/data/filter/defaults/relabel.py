"""Default item label restylings.

IMPORTANT: Item names are rendered bottom-up, for both composed and self-complete item names!
---------------------------------------------------------------------------------------------
e.g. 1) if you wanted 'haha' *above* an item name, you would "\n  {name}  \n  haha  \n"
e.g. 2) a colour tag *terminating* an item name will apply to the row above it.
      - "{orange}Diadem" would mean 'Griffon's Eye' displays above it in unique colour.
      - "{orange}Diadem{white}" would mean the "Griffon's Eye" line renders white!
"""
from ..styling import decoration


# Many label restyles copy from or iterate on (with permission) AlexisEvo's original work
# https://github.com/AlexisEvo/d2r-loot-filter
ITEMS = (
    {
        # key — removed by default, but styled since it can smooth out LK run pit stops
        "key": "key",
        "name":  "{grey}[{gold}k{grey}]",
        "compact_name": "{grey}[ {gold}k{grey} ]",
    },
    # ------------------------------------------------ regen potions
    {
        # super healing potion
        "key": "hp5",
        "name":  "{red}health{white}POT",
        "compact_name": "{red}h{white}POT",
    },
    {
        # super mana potion
        "key": "mp5",
        "name":  "{blue}mana{white}POT",
        "compact_name": "{blue}m{white}POT",
    },
    {
        # rejuvenation potion
        "key": "rvs",
        "name":  "{purple}35{white}juv",
        "compact_name": "{purple}35{white}j",
    },
    {
        # rejuvenation potion
        "key": "rvl",
        "name":  "{purple}FULL{white}juv",
        "compact_name": "{purple}FULL{white}j",
    },
    # ------------------------------------------------ scrolls & tomes
    {
        # scroll of town portal
        "key": "tsc",
        "name":  "{blue}§{white}tp",
        "compact_name": "{blue}§",
    },
    {
        # tome of town portal
        "key": "tbk",
        "name":  "{blue}§{white}tome",
        "compact_name": "{blue}§{white}[]",
    },
    {
        # scroll of identify
        "key": "isc",
        "name":  "{red}§{white}id",
        "compact_name": "{red}§",
    },
    {
        # tome of identify
        "key": "ibk",
        "name":  "{red}§{white}tome",
        "compact_name": "{red}§{white}[]",
    },
)


AFFIXES = (
    {
        # gold
        "key": "glg",
        "name":  "{gold}g",
        "compact_name": "{gold}g",
    },
)


# N.B. Latent "{}" placeholder only works with .format(), not f-string
RUNES = {
    # TODO: make HR/MR ranks composable. default: non-hellforge floor
    "high": {
        "label_wrapper": "\n~         {name}         ~\n{purple}~        ~ ! g g ! ~       ~\n",
        "rank_range":    (26, 33),  # vex -> zod
    },
    "mid": {
        "label_wrapper": "~    {name}    ~\n{purple}~   ~ ! -- ! ~   ~",
        "rank_range":    (20, 25),  # lem -> gul
    },
}
