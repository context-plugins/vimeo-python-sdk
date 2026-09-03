from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Stream2(str, Enum):
    """The user's streaming access to the On Demand subscription.

    Option descriptions:
     * ``available`` - The On Demand subscription is available for streaming.
     * ``purchased`` - The On Demand subscription has been purchased.
     * ``restricted`` - Streaming for the On Demand subscription is restricted.
     * ``unavailable`` - The On Demand subscription is unavailable."""

    AVAILABLE = "available"
    PURCHASED = "purchased"
    RESTRICTED = "restricted"
    UNAVAILABLE = "unavailable"

    __str__ = str.__str__


Stream2OrStr: TypeAlias = Annotated[Stream2 | str, open_enum_validator(Stream2)]
