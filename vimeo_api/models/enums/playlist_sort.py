from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PlaylistSort(str, Enum):
    """The order in which the videos inside the event appear in the playlist.

    Option descriptions:
     * ``added_first`` - The videos appear according to when they were added to the event, with the most recently added
            first.
     * ``added_last`` - The videos appear according to when they were added to the event, with the most recently added
            last.
     * ``alphabetical`` - The videos appear alphabetically by their title.
     * ``arranged`` - The videos appear as arranged by the owner of the event.
     * ``comments`` - The videos appear according to their number of comments.
     * ``duration`` - The videos appear in order of duration.
     * ``likes`` - The videos appear according to their number of likes.
     * ``newest`` - The videos appear in chronological order, with the newest first.
     * ``oldest`` - The videos appear in chronological order, with the oldest first.
     * ``plays`` - The videos appear according to their number of plays."""

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


PlaylistSortOrStr: TypeAlias = Annotated[PlaylistSort | str, open_enum_validator(PlaylistSort)]
