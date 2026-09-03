from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Status18(str, Enum):
    """The status of the team membership invite.

    Option descriptions:
     * ``accepted`` - Team membership has been accepted.
     * ``pending`` - Team membership has been offered but not yet accepted."""

    ACCEPTED = "accepted"
    PENDING = "pending"

    __str__ = str.__str__


Status18OrStr: TypeAlias = Annotated[Status18 | str, open_enum_validator(Status18)]
