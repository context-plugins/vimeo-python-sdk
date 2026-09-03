from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Comments2(str, Enum):
    """The video's comment permission setting.

    Option descriptions:
     * ``anybody`` - Anyone can comment on the video.
     * ``contacts`` - Only contacts can comment on the video.
     * ``nobody`` - No one can comment on the video."""

    ANYBODY = "anybody"
    CONTACTS = "contacts"
    NOBODY = "nobody"

    __str__ = str.__str__


Comments2OrStr: TypeAlias = Annotated[Comments2 | str, open_enum_validator(Comments2)]
