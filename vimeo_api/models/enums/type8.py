from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type8(str, Enum):
    """The user's role type. This data requires a bearer token with the ``private`` scope.

    Option descriptions:
     * ``member`` - The user is a member.
     * ``moderator`` - The user is a moderator."""

    MEMBER = "member"
    MODERATOR = "moderator"

    __str__ = str.__str__


Type8OrStr: TypeAlias = Annotated[Type8 | str, open_enum_validator(Type8)]
