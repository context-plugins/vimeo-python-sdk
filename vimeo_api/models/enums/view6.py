from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class View6(str, Enum):
    """The access level of the showcase.

    Option descriptions:
     * ``anybody`` - Anyone can access the showcase. This privacy setting appears as ``Public`` on the Vimeo front end.
     * ``embed_only`` - The showcase doesn't appear on Vimeo, but the owner can embed it on other sites.
     * ``nobody`` - No one can access the showacse, including the owner. This privacy setting appears as ``Private`` on
            the Vimeo front end.
     * ``password`` - Only those with the password can access the showcase.
     * ``team`` - Only the owner and members of the owner's team can access the showcase.
     * ``unlisted`` - The showcase can't be accessed if the URL omits its unlisted hash."""

    ANYBODY = "anybody"
    EMBED_ONLY = "embed_only"
    NOBODY = "nobody"
    PASSWORD = "password"
    TEAM = "team"
    UNLISTED = "unlisted"

    __str__ = str.__str__


View6OrStr: TypeAlias = Annotated[View6 | str, open_enum_validator(View6)]
