from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Projection1(str, Enum):
    """The 360 spatial projection.

    Option descriptions:
     * ``cubical`` - Use cubical projection.
     * ``cylindrical`` - Use cylindrical projection.
     * ``dome`` - Use dome projection.
     * ``equirectangular`` - Use equirectangular projection.
     * ``pyramid`` - Use pyramid projection."""

    CUBICAL = "cubical"
    CYLINDRICAL = "cylindrical"
    DOME = "dome"
    EQUIRECTANGULAR = "equirectangular"
    PYRAMID = "pyramid"

    __str__ = str.__str__


Projection1OrStr: TypeAlias = Annotated[Projection1 | str, open_enum_validator(Projection1)]
