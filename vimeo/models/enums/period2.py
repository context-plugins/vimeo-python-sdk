from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Period2(str, Enum):
    """The time period for which the DRM usage activity is evaluated.

    Option descriptions:
     * ``lifetime`` - The quota period is for the lifetime of the account.
     * ``year`` - The quota period is one year."""

    LIFETIME = "lifetime"
    YEAR = "year"

    __str__ = str.__str__


Period2OrStr: TypeAlias = Annotated[Period2 | str, open_enum_validator(Period2)]
