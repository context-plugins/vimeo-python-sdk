from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class View(str, Enum):
    """The privacy setting of the channel.

    Option descriptions:
     * ``anybody`` - Anyone can access the channel. This privacy setting appears as ``Public`` on the Vimeo front end.
     * ``moderators`` - Only moderators can access the channel.
     * ``users`` - Only registered users can access the channel. _This field is deprecated._"""

    ANYBODY = "anybody"
    MODERATORS = "moderators"
    USERS = "users"

    __str__ = str.__str__


ViewOrStr: TypeAlias = Annotated[View | str, open_enum_validator(View)]
