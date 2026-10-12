from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type22(str, Enum):
    """The way in which the promotion generates promo codes.

    Option descriptions:
     * ``batch`` - The promotion provides a unique promotional code for each user.
     * ``batch_prefix`` - Like ``batch``, except that all codes have a similar prefix string. _This option is
            deprecated, yet it may still appear for some users._
     * ``single`` - The promotion provides a single promotional code for all users."""

    BATCH = "batch"
    BATCH_PREFIX = "batch_prefix"
    SINGLE = "single"

    __str__ = str.__str__


Type22OrStr: TypeAlias = Annotated[Type22 | str, open_enum_validator(Type22)]
