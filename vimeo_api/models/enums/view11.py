from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class View11(str, Enum):
    """Who can access the user's videos by default.

    Option descriptions:
     * ``anybody`` - Anyone can access the videos. This privacy setting appears as ``Public`` on the Vimeo front end.
     * ``contacts`` - Only the user's contacts can access the videos. _This field is deprecated._
     * ``disable`` - The videos are disabled. This privacy setting appears as ``Embed only`` on the Vimeo front end.
     * ``nobody`` - No one can access the videos. This privacy setting appears as ``Private`` on the Vimeo front end.
     * ``password`` - Only those with the password can access the videos.
     * ``unlisted`` - The videos are unlisted.
     * ``users`` - Only other Vimeo members can access the videos. _This field is deprecated._"""

    ANYBODY = "anybody"
    CONTACTS = "contacts"
    DISABLE = "disable"
    NOBODY = "nobody"
    PASSWORD = "password"
    UNLISTED = "unlisted"
    USERS = "users"

    __str__ = str.__str__


View11OrStr: TypeAlias = Annotated[View11 | str, open_enum_validator(View11)]
