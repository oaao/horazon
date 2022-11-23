"""Default configurations."""

from .styling import colours as _


REMOVE_ITEMS = (
    # ------------------------------------------------ regen potions
    "hp1",  # healing, minor
    "hp2",  # healing, light
    "hp3",  # healing
    "hp4",  # healing, greater
    "mp1",  # mana, minor
    "mp2",  # mana, light
    "mp3",  # mana
    "mp4",  # mana, greater
    # ------------------------------------------------ utility potions
    "gpl",  # strangling gas
    "gpm",  # choking gas potion
    "gps",  # rancid gas potion
    "opl",  # fulminating gas potion
    "opm",  # exploding gas potion
    "ops",  # oil potion
    "vps",  # stamina
    "wms",  # thawing potion
    "yps",  # antidote potion
    # ------------------------------------------------ ammunition & keys
    "aqv",  # arrows
    "cqv",  # bolts
    "key",  # key
    # ------------------------------------------------ gems (flawed, chipped, ~regular)
    "gcv",  # amethyst, chipped
    "gfv",  # amethyst, flawed
    "gcy",  # topaz, chipped
    "gfy",  # topaz, flawed
    "gsy",  # topaz
    "gcb",  # sapphire, chipped
    "gfb",  # sapphire, flawed
    "gcg",  # emerald, chipped
    "gfg",  # emerald, flawed
    "gcr",  # ruby, chipped
    "gfr",  # ruby, flawed
    "gcw",  # diamond, chipped
    "gfw",  # diamond, flawed
    "skc",  # skull, chipped
    "skf",  # skull, flawed
    "sku",
    """
    In the game files, the other *regular* gems live in item-nameaffixes.json. See below.
    """
)



REMOVE_AFFIXES = (
    # ------------------------------------------------ gems (all other regular gems)
    "gsb",  # sapphire
    "gsg",  # emerald
    "gsr",  # ruby
    "gsw",  # diamond
    """
    Putting the above reg gems in item-names.json instead of item-nameaffixes.json causes
    undefined item fallback text ("An Evil Force") to display.
    """
)


# Many label restyles copy from or iterate on (with permission) AlexisEvo's original work
# https://github.com/AlexisEvo/d2r-loot-filter
RESTYLE_ITEMS = (
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


RESTYLE_AFFIXES = (
    {
        # gold
        "key": "glg",
        "long_name": f"{_.GOLD}g",
        "short_name": f"{_.GOLD}g",
    },
)
