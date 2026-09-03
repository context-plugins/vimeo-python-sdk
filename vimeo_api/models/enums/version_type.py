from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class VersionType(str, Enum):
    """The type of the version.

    Option descriptions:
     * ``regular`` - The version was generated through a file upload.
     * ``screen-recording`` - The version was generated through Vimeo Record.
     * ``vimeo-create`` - The version was generated through Vimeo Create."""

    REGULAR = "regular"
    SCREEN_RECORDING = "screen-recording"
    VIMEO_CREATE = "vimeo-create"

    __str__ = str.__str__


VersionTypeOrStr: TypeAlias = Annotated[VersionType | str, open_enum_validator(VersionType)]
