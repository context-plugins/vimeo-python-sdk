from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Privacy12(str, Enum):
    """The privacy level of the showcase.

    Option descriptions:
     * ``anybody`` - Anyone can access the showcase, either on Vimeo or through an embed.
     * ``embed_only`` - The showcase doesn't appear on Vimeo, but it can be embedded on other sites.
     * ``nobody`` - No one can access the showcase, including the authenticated user.
     * ``password`` - Only people with the password can access the showcase.
     * ``team`` - Only members of the authenticated user's team can access the showcase.
     * ``unlisted`` - The showcase can't be accessed if the URL omits its unlisted hash."""

    ANYBODY = "anybody"
    EMBED_ONLY = "embed_only"
    NOBODY = "nobody"
    PASSWORD = "password"
    TEAM = "team"
    UNLISTED = "unlisted"

    __str__ = str.__str__


Privacy12OrStr: TypeAlias = Annotated[Privacy12 | str, open_enum_validator(Privacy12)]
