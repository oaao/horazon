"""Processing functionality for contextual & indexical item data."""
from typing import union

from .. import data


D2R_DATA_PATH = data.__path__ + "/d2r"

DROPS_SUBPATH = D2R_DATA_PATH + "/local/lng/strings/"

ITEMS_SUBPATH = DROPS_SUBPATH + "item-names.json"
AFFIX_SUBPATH = DROPS_SUBPATH + "item-nameaffixes.json"
RUNES_SUBPATH = DROPS_SUBPATH + "item-runes.json"


# TODO: runtime loader of {"id", "key", "enUS" [, "data_path"]} of all item-like entities
# TODO: this may be best as a dict wrapper class with overridden access methods
def load_items() -> tuple[dict[str, str]]:
    # TODO: path should be optional against a dict.get() default of {ITEMS_SUBPATH}.
    # TODO: ^ a loader for this that maps {key:filepath} for affix/rune entities.
    # TODO: name_{lang} fields for languages
    pass


def get_item(code: Union[int, str]) -> dict[str, str]:
    """Retrieve an item dictionary from mem-loaded reference data.

        code:      numerical ID, or string key
        -> return: dict with {'key', 'name', 'tags'}
    """
    match code:
        case int(): pass  # get item via id
        case str(): pass  # get item via key 
    # TODO: get_item() should probably also pack in that item's context tag dict
    return {
        "key":  "",
        "name": "",
        # "tags": {},
    }