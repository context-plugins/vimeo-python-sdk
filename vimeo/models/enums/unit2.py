from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Unit2(str, Enum):
    """The unit that's used to compute quota.

    Option descriptions:
     * ``video_size`` - The quota is calculated using the byte size of the videos."""

    VIDEO_SIZE = "video_size"

    __str__ = str.__str__


Unit2OrStr: TypeAlias = Annotated[Unit2 | str, open_enum_validator(Unit2)]
