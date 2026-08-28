from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Embed19(str, Enum):
    """The video's embed setting. Specify the ``whitelist`` value to restrict embedding to a specific set of domains.
    For more information, see our `Interacting with Videos
    <https://developer.vimeo.com/api/guides/videos/interact#set-off-site-privacy>`__ guide.

    Option descriptions:
     * ``private`` - The video can't be embedded.
     * ``public`` - The video can be embedded.
     * ``whitelist`` - The video can be embedded on the specified domains only."""

    PRIVATE = "private"
    PUBLIC = "public"
    WHITELIST = "whitelist"

    __str__ = str.__str__


Embed19OrStr: TypeAlias = Annotated[Embed19 | str, open_enum_validator(Embed19)]
