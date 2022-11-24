"""Items filtered out by default."""


ITEMS = (
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


AFFIXES = (
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
