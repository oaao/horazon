"""Default item label restylings.

IMPORTANT: Item names are rendered bottom-up, for both composed and self-complete item names!
---------------------------------------------------------------------------------------------
e.g. 1) if you wanted 'haha' *above* an item name, you would "\n  {name}  \n  haha  \n"
e.g. 2) a colour tag *terminating* an item name will apply to the row above it.
      - "{orange}Diadem" would mean 'Griffon's Eye' displays above it in unique colour.
      - "{orange}Diadem{white}" would mean the "Griffon's Eye" line renders white!
"""


# Many label restyles copy from or iterate on (with permission) AlexisEvo's original work
# https://github.com/AlexisEvo/d2r-loot-filter
ITEMS = (
    {
        # key — removed by default, but styled since it can smooth out LK run pit stops
        "key": "key",
        "long_name":  "{grey}[{gold}k{grey}]",
        "short_name": "{grey}[ {gold}k{grey} ]",
    },
    # ------------------------------------------------ regen potions
    {
        # super healing potion
        "key": "hp5",
        "long_name":  "{red}health{white}POT",
        "short_name": "{red}h{white}POT",
    },
    {
        # super mana potion
        "key": "mp5",
        "long_name":  "{blue}mana{white}POT",
        "short_name": "{blue}m{white}POT",
    },
    {
        # rejuvenation potion
        "key": "rvs",
        "long_name":  "{purple}35{white}juv",
        "short_name": "{purple}35{white}j",
    },
    {
        # rejuvenation potion
        "key": "rvl",
        "long_name":  "{purple}FULL{white}juv",
        "short_name": "{purple}FULL{white}j",
    },
    # ------------------------------------------------ scrolls & tomes
    {
        # scroll of town portal
        "key": "tsc",
        "long_name":  "{blue}§{white}tp",
        "short_name": "{blue}§",
    },
    {
        # tome of town portal
        "key": "tbk",
        "long_name":  "{blue}§{white}tome",
        "short_name": "{blue}§{white}[]",
    },
    {
        # scroll of identify
        "key": "isc",
        "long_name":  "{red}§{white}id",
        "short_name": "{red}§",
    },
    {
        # tome of identify
        "key": "ibk",
        "long_name":  "{red}§{white}tome",
        "short_name": "{red}§{white}[]",
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
        "long_name":  "{gold}g",
        "short_name": "{gold}g",
    },
)


# N.B. Latent "{}" placeholder only works with .format(), not f-string
RUNES = {
    # TODO: make HR/MR ranks composable. default: non-hellforge floor
    "high": {
        "label_wrapper": ,
        "rank_range":    (26, 33),  # vex -> zod
    },
    "mid": {
        "label_wrapper": ,
        "rank_range":    (20, 25),  # lem -> gul
    }
}
