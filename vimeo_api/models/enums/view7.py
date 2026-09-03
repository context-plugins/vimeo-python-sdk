from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class View7(str, Enum):
    """The general privacy setting for generated videos and the embed privacy of the entire collection.

    Option descriptions:
     * ``anybody`` - Anyone can access the videos. This privacy setting appears as ``Public`` on the Vimeo front end.
     * ``embed_only`` - The videos don't appear on Vimeo, but they can be embedded elsewhere.
     * ``nobody`` - Only the event owner can access the videos. This privacy setting appears as ``Private`` on the Vimeo
            front end.
     * ``password`` - Only those with the password can access the videos.
     * ``team`` - Anyone on this team can access the videos. This privacy setting appears as ``Company only`` on the
            Vimeo front end.
     * ``unlisted`` - Only those with the private link can access the videos."""

    ANYBODY = "anybody"
    EMBED_ONLY = "embed_only"
    NOBODY = "nobody"
    PASSWORD = "password"
    TEAM = "team"
    UNLISTED = "unlisted"

    __str__ = str.__str__


View7OrStr: TypeAlias = Annotated[View7 | str, open_enum_validator(View7)]
