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
    # ------------------------------------------------ gems (flawless & perfect)
    {
        # flawless amethyst
        "key":  "gzv",
        "name": "{purple}" + decoration.FLAWLESS,
    },
    {
        # perfect amethyst
        "key":  "gpv",
        "name": "{purple}" + decoration.PERFECT,
    },
    {
        # flawless topaz
        "key":  "gly",
        "name": "{yellow}" + decoration.FLAWLESS,
    },
    {
        # perfect topaz
        "key":  "gpy",
        "name": "{yellow}" + decoration.PERFECT,
    },
    {
        # flawless sapphire
        "key":  "glb",
        "name": "{blue}" + decoration.FLAWLESS,
    },
    {
        # perfect sapphire
        "key":  "gpb",
        "name": "{blue}" + decoration.PERFECT,
    },
    {
        # flawless emerald
        "key":  "glg",
        "name": "{lime}" + decoration.FLAWLESS,
    },
    {
        # perfect emerald
        "key":  "gpg",
        "name": "{lime}" + decoration.PERFECT,
    },
    {
        # flawless ruby
        "key":  "glr",
        "name": "{red}" + decoration.FLAWLESS,
    },
    {
        # perfect ruby
        "key":  "gpr",
        "name": "{red}" + decoration.PERFECT,
    },
    {
        # flawless diamond
        "key":  "glw",
        "name": "{white}" + decoration.FLAWLESS,
    },
    {
        # perfect diamond
        "key":  "gpw",
        "name": "{white}" + decoration.PERFECT,
    },
    {
        # flawless skull
        "key":  "skl",
        "name": "{grey}" + decoration.FLAWLESS,
    },
    {
        # perfect skull
        "key":  "skz",
        "name": "{grey}" + decoration.PERFECT,
    },

    # ------------------------------------------------ jewels & charms (small & grand)
    {
        # small charm
        "key":  "cm1",
        "name": decoration.PAD.format(name="Small"),
        "compact_name": decoration.PAD.format(name="Sc"),
    },
    {
        # grand charm — N.B. changing its colour undifferentiates Gheed's!
        "key":  "cm3",
        "name": decoration.PAD.format(name="Srand"),
        "compact_name": decoration.PAD.format(name="Gc"),
    },
    {
        # jewels
        "key":  "jew",
        "name": decoration.PAD.format(name="Jewel"),
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
        "label_wrapper": decoration.HR,
        "rank_range":    (26, 33),  # vex -> zod
    },
    "mid": {
        "label_wrapper": decoration.MR,
        "rank_range":    (20, 25),  # lem -> gul
    },
}
