from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PlaylistSort2(str, Enum):
    """The order in which the videos of the event appear within the event's playlist.

    Option descriptions:
     * ``added_first`` - The most recently added videos appear first.
     * ``added_last`` - The most recently added videos appear last.
     * ``alphabetical`` - The videos appear in alphabetical order.
     * ``arranged`` - The videos appear in the order in which the user has arranged them.
     * ``comments`` - The videos appear in order of number of comments.
     * ``duration`` - The videos appear in order of duration.
     * ``likes`` - The videos appear in order of number of likes.
     * ``newest`` - The newest videos appear first.
     * ``oldest`` - The oldest videos appear first.
     * ``plays`` - The videos appear in order of number of plays."""

    ADDED_FIRST = "added_first"
    ADDED_LAST = "added_last"
    ALPHABETICAL = "alphabetical"
    ARRANGED = "arranged"
    COMMENTS = "comments"
    DURATION = "duration"
    LIKES = "likes"
    NEWEST = "newest"
    OLDEST = "oldest"
    PLAYS = "plays"

    __str__ = str.__str__


PlaylistSort2OrStr: TypeAlias = Annotated[PlaylistSort2 | str, open_enum_validator(PlaylistSort2)]
