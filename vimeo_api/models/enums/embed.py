from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Embed(str, Enum):
    """The authenticated user's privacy preference for embeds.

    Option descriptions:
     * ``private`` - Only the user can embed their own videos.
     * ``public`` - Anyone can embed the user's videos.
     * ``whitelist`` - Only specified users can embed the user's videos."""

    PRIVATE = "private"
    PUBLIC = "public"
    WHITELIST = "whitelist"

    __str__ = str.__str__


EmbedOrStr: TypeAlias = Annotated[Embed | str, open_enum_validator(Embed)]
