from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Sort(str, Enum):
    """The sort order of the showcase.

    Option descriptions:
     * ``added_first`` - Sort the showcase videos in order of those most recently added.
     * ``added_last`` - Sort the showcase videos in order of those least recently added.
     * ``alphabetical`` - Sort the showcase videos alphabetically.
     * ``arranged`` - Sort the showcase videos according to their custom arrangement.
     * ``comments`` - Sort the showcase videos by number of comments.
     * ``likes`` - Sort the showcase videos by number of likes.
     * ``newest`` - Sort the showcase videos in order of creation date with the newest first.
     * ``oldest`` - Sort the showcase videos in order of creation date with the oldest first.
     * ``plays`` - Sort the showcase videos by number of plays."""

    ADDED_FIRST = "added_first"
    ADDED_LAST = "added_last"
    ALPHABETICAL = "alphabetical"
    ARRANGED = "arranged"
    COMMENTS = "comments"
    LIKES = "likes"
    NEWEST = "newest"
    OLDEST = "oldest"
    PLAYS = "plays"

    __str__ = str.__str__


SortOrStr: TypeAlias = Annotated[Sort | str, open_enum_validator(Sort)]
