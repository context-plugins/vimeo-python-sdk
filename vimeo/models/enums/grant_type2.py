from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class GrantType2(str, Enum):
    """The grant type. The value of this field must be ``vimeo_oauth1``.

    Option descriptions:
     * ``vimeo_oauth1`` - The grant type is for the OAuth1 token."""

    VIMEO_OAUTH1 = "vimeo_oauth1"

    __str__ = str.__str__


GrantType2OrStr: TypeAlias = Annotated[GrantType2 | str, open_enum_validator(GrantType2)]
