from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Sort1(str, Enum):
    """The default video sort order of the portfolio.

    Option descriptions:
     * ``alphabetical`` - The default sort order is alphabetical by name.
     * ``clips`` - The default sort order is video creation date.
     * ``modified`` - The default sort order is the order in which the videos were modified.
     * ``recent`` - The default sort order is the order in which the videos were added."""

    ALPHABETICAL = "alphabetical"
    CLIPS = "clips"
    MODIFIED = "modified"
    RECENT = "recent"

    __str__ = str.__str__


Sort1OrStr: TypeAlias = Annotated[Sort1 | str, open_enum_validator(Sort1)]
