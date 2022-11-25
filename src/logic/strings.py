import string

from . import items
from ..data.filter.styling import colours


COLOUR_MAP = {
    c.lower(): getattr(colours, c)
    for c in dir(colours)
    if not c.startswith("__")
}


def get_string_fields(s: str) -> tuple[str]:
    """Get the latent fieldnames of a pre-.format()tted string."""
    return tuple(
        (
            fieldname
            for text, fieldname, * in string.Formatter().parse(s)
            if fieldname is not None
        )
    )


def format_latent_string(s : str, key: str) -> str:
    """Finalise a latent string with data & styling elements."""
    fields = get_string_fields(s)
    _map   = {
        k: v
        for k, v in COLOUR_MAP.items()
        if k in fields
    }
    if "name" in fields:
        _map.update({"name": items.get_item(key)})
    # calling str.format() with missing/excess keys -> KeyError
    # TODO: decide if this unhandled/loud failure is desirable
    return s.format(**_map)
