from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class License(str, Enum):
    """The `Creative Commons <http://creativecommons.org/licenses/>`__ license that the user has set to be the default.

    Option descriptions:
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


LicenseOrStr: TypeAlias = Annotated[License | str, open_enum_validator(License)]
