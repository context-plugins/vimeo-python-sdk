from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Download(str, Enum):
    """The user's download access to the On Demand video.

    Option descriptions:
     * ``available`` - The video is available for download.
     * ``purchased`` - The user has purchased the video.
     * ``restricted`` - The user isn't permitted to download the video.
     * ``unavailable`` - The video isn't available for download."""

    AVAILABLE = "available"
    PURCHASED = "purchased"
    RESTRICTED = "restricted"
    UNAVAILABLE = "unavailable"

    __str__ = str.__str__


DownloadOrStr: TypeAlias = Annotated[Download | str, open_enum_validator(Download)]
