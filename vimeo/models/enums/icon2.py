from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Icon2(str, Enum):
    """An icon that represents the reason why publish-to-social presets are disabled.

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


Icon2OrStr: TypeAlias = Annotated[Icon2 | str, open_enum_validator(Icon2)]
