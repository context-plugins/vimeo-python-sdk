from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class State(str, Enum):
    """The status of the destination.

    Option descriptions:
     * ``0`` - The status is OK.
     * ``1`` - An error occurred. Check the ``state_message`` field for details."""

    _0 = "0"
    _1 = "1"

    __str__ = str.__str__


StateOrStr: TypeAlias = Annotated[State | str, open_enum_validator(State)]
