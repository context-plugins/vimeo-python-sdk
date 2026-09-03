from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Icon1(str, Enum):
    """An icon that represents the reason why available showcase presets are disabled. This data requires a bearer token
    with the ``private`` scope.

    Option descriptions:
     * ``clock`` - The reason is represented by a clock icon.
     * ``create`` - The reason is represented by a create icon.
     * ``image`` - The reason is represented by an image icon.
     * ``theme`` - The reason is represented by a theme icon."""

    CLOCK = "clock"
    CREATE = "create"
    IMAGE = "image"
    THEME = "theme"

    __str__ = str.__str__


Icon1OrStr: TypeAlias = Annotated[Icon1 | str, open_enum_validator(Icon1)]
