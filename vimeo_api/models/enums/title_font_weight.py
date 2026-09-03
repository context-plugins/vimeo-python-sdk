from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class TitleFontWeight(int, Enum):
    """The selected video title font weight.

    Option descriptions:
     * ``300`` - Light
     * ``400`` - Regular
     * ``500`` - Medium
     * ``700`` - Bold"""

    VALUE_300 = 300
    VALUE_400 = 400
    VALUE_500 = 500
    VALUE_700 = 700

    __str__ = str.__str__


TitleFontWeightOrInt: TypeAlias = Annotated[TitleFontWeight | int, open_enum_validator(TitleFontWeight)]
