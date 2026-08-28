from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type1(str, Enum):
    """The authenticated user's role type. This data requires a bearer token with the ``private`` scope.

    Option descriptions:
     * ``moderator`` - The authenticated user is a moderator.
     * ``subscriber`` - The authenticated user is a subscriber."""

    MODERATOR = "moderator"
    SUBSCRIBER = "subscriber"

    __str__ = str.__str__


Type1OrStr: TypeAlias = Annotated[Type1 | str, open_enum_validator(Type1)]
