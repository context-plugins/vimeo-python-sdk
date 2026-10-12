from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type19(str, Enum):
    """The type of the simulcast destination.

    Option descriptions:
     * ``channel`` - The destination is a YouTube channel.
     * ``custom`` - The destination is custom.
     * ``organization`` - The destination is a LinkedIn organization.
     * ``page`` - The destination is a Facebook page.
     * ``profile`` - The destination is a Facebook or LinkedIn profile."""

    CHANNEL = "channel"
    CUSTOM = "custom"
    ORGANIZATION = "organization"
    PAGE = "page"
    PROFILE = "profile"

    __str__ = str.__str__


Type19OrStr: TypeAlias = Annotated[Type19 | str, open_enum_validator(Type19)]
