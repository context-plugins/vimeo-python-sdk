from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class View1(str, Enum):
    """The authenticated user's privacy preference for views.

    Option descriptions:
     * ``anybody`` - Anyone can view the user's videos. This privacy setting appears as ``Public`` on the Vimeo front
            end.
     * ``contacts`` - Only contacts can view the user's videos. _This field is deprecated._
     * ``disable`` - Views are disabled for the user's videos. This privacy setting appears as ``Embed only`` on the
            Vimeo front end.
     * ``nobody`` - No one except the user can view the user's videos. This privacy setting appears as ``Private`` on
            the Vimeo front end.
     * ``password`` - Only those with the password can view the user's videos.
     * ``unlisted`` - Anybody can view the user's videos if they have a link.
     * ``users`` - Only other Vimeo members can view the user's videos. _This field is deprecated._"""

    ANYBODY = "anybody"
    CONTACTS = "contacts"
    DISABLE = "disable"
    NOBODY = "nobody"
    PASSWORD = "password"
    UNLISTED = "unlisted"
    USERS = "users"

    __str__ = str.__str__


View1OrStr: TypeAlias = Annotated[View1 | str, open_enum_validator(View1)]
