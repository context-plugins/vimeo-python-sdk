from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Privacy9(str, Enum):
    """The privacy setting of the destination. Be sure to choose a value that corresponds to your service.

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


Privacy9OrStr: TypeAlias = Annotated[Privacy9 | str, open_enum_validator(Privacy9)]
