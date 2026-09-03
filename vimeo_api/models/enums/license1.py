from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class License1(str, Enum):
    """The `Creative Commons <http://creativecommons.org/licenses/>`__ license that the video is given under.

    Option descriptions:
     * `` - No Creative Commons license has been set for the video.
     * ``by`` - The video is given under the Attribution license.
     * ``by-nc`` - The video is given under the Attribution Non-Commercial license.
     * ``by-nc-nd`` - The video is given under the Attribution Non-Commercial No Derivatives license.
     * ``by-nc-sa`` - The video is given under the Attribution Non-Commercial Share Alike license.
     * ``by-nd`` - The video is given under the Attribution No Derivatives license.
     * ``by-sa`` - The video is given under the Attribution Share Alike license.
     * ``cc0`` - The video is given under the Public Domain Dedication license."""

    BY = "by"
    BY_NC = "by-nc"
    BY_NC_ND = "by-nc-nd"
    BY_NC_SA = "by-nc-sa"
    BY_ND = "by-nd"
    BY_SA = "by-sa"
    CC0 = "cc0"

    __str__ = str.__str__


License1OrStr: TypeAlias = Annotated[License1 | str, open_enum_validator(License1)]
