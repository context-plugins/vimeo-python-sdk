from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Code1(str, Enum):
    """The type of Creative Commons license.

    Option descriptions:
     * ``by`` - Attribution.
     * ``by-nc`` - Attribution Non-Commercial.
     * ``by-nc-nd`` - Attribution Non-Commercial No Derivatives.
     * ``by-nc-sa`` - Attribution Non-Commercial Share Alike.
     * ``by-nd`` - Attribution No Derivatives.
     * ``by-sa`` - Attribution Share Alike.
     * ``cc0`` - Public Domain Dedication."""

    BY = "by"
    BY_NC = "by-nc"
    BY_NC_ND = "by-nc-nd"
    BY_NC_SA = "by-nc-sa"
    BY_ND = "by-nd"
    BY_SA = "by-sa"
    CC0 = "cc0"

    __str__ = str.__str__


Code1OrStr: TypeAlias = Annotated[Code1 | str, open_enum_validator(Code1)]
