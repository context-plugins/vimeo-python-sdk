from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Mode(str, Enum):
    """The team seats mode for the user's team.

    Option descriptions:
     * ``admin_and_authenticated`` - The mode for Enterprise-Base Platform, Enterprise-Marketing, and Enterprise-Central
            users.
     * ``global`` - The default mode for legacy and self-serve users.
     * ``per_seat_type`` - The mode for sales-assisted users, including Enterprise, Custom, and Custom OTT."""

    ADMIN_AND_AUTHENTICATED = "admin_and_authenticated"
    GLOBAL = "global"
    PER_SEAT_TYPE = "per_seat_type"

    __str__ = str.__str__


ModeOrStr: TypeAlias = Annotated[Mode | str, open_enum_validator(Mode)]
