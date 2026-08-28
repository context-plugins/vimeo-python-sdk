from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Projection(str, Enum):
    """The video's 360 spatial projection.

    Option descriptions:
     * ``cubical`` - The spatial projection is cubical.
     * ``cylindrical`` - The spatial projection is cylindrical.
     * ``dome`` - The spatial projection is dome-shaped.
     * ``equirectangular`` - The spatial projection is equirectangular.
     * ``pyramid`` - The spatial projection is pyramid-shaped."""

    CUBICAL = "cubical"
    CYLINDRICAL = "cylindrical"
    DOME = "dome"
    EQUIRECTANGULAR = "equirectangular"
    PYRAMID = "pyramid"

    __str__ = str.__str__


ProjectionOrStr: TypeAlias = Annotated[Projection | str, open_enum_validator(Projection)]
