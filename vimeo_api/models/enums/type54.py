from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type54(str, Enum):
    """The widget variant.

    Option descriptions:
     * ``ranking`` - The widget shows a ranking of options.
     * ``thumbs`` - The widget shows thumbs up/down buttons."""

    RANKING = "ranking"
    THUMBS = "thumbs"

    __str__ = str.__str__


Type54OrStr: TypeAlias = Annotated[Type54 | str, open_enum_validator(Type54)]
