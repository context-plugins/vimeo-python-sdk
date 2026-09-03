from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Privacy6(str, Enum):
    """The privacy setting of the destination.

    Option descriptions:
     * ``CONNECTIONS`` - The privacy setting is ``CONNECTIONS`` for LinkedIn.
     * ``PUBLIC`` - The privacy setting is ``PUBLIC`` for LinkedIn.
     * ``all_friends`` - The privacy setting is ``all_friends`` for Facebook.
     * ``everyone`` - The privacy setting is ``everyone`` for Facebook.
     * ``private`` - The privacy setting is ``private`` for YouTube.
     * ``public`` - The privacy setting is ``public`` for YouTube.
     * ``self`` - The privacy setting is ``self`` for Facebook.
     * ``unlisted`` - The privacy setting is ``unlisted`` for YouTube."""

    CONNECTIONS = "CONNECTIONS"
    PUBLIC = "PUBLIC"
    ALL_FRIENDS = "all_friends"
    EVERYONE = "everyone"
    PRIVATE = "private"
    PUBLIC2 = "public"
    SELF = "self"
    UNLISTED = "unlisted"

    __str__ = str.__str__


Privacy6OrStr: TypeAlias = Annotated[Privacy6 | str, open_enum_validator(Privacy6)]
