from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Embed11(str, Enum):
    """The privacy for the user's embedded videos. The ``whitelist`` value enables you to define all valid embeddable
    domains. See our `Interacting with Videos
    <https://developer.vimeo.com/api/guides/videos/interact#set-off-site-privacy>`__ guide for details on adding and
    removing domains.

    Option descriptions:
     * ``private`` - The videos can't be embedded on any domain.
     * ``public`` - The videos can be embedded on any domain.
     * ``whitelist`` - The videos can be embedded on the specified domains only."""

    PRIVATE = "private"
    PUBLIC = "public"
    WHITELIST = "whitelist"

    __str__ = str.__str__


Embed11OrStr: TypeAlias = Annotated[Embed11 | str, open_enum_validator(Embed11)]
