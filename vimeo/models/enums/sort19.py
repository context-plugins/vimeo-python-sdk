from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Sort19(str, Enum):
    """The default sort order of the videos as they appear in the showcase.

    Option descriptions:
     * ``added_first`` - The videos appear according to when they were added to the showcase, with the most recently
            added first.
     * ``added_last`` - The videos appear according to when they were added to the showcase, with the most recently
            added last.
     * ``alphabetical`` - The videos appear alphabetically by their title.
     * ``alphabetical_desc`` - The videos appear alphabetically by their title in reverse order.
     * ``arranged`` - The videos appear as arranged by the owner of the showcase.
     * ``comments`` - The videos appear according to their number of comments.
     * ``likes`` - The videos appear according to their number of likes.
     * ``modified_time_asc`` - The videos appear in ascending order based on their last modified time.
     * ``modified_time_desc`` - The videos appear in descending order based on their last modified time.
     * ``newest`` - The videos appear in chronological order with the newest first.
     * ``oldest`` - The videos appear in chronological order with the oldest first.
     * ``plays`` - The videos appear according to their number of plays."""

    ADDED_FIRST = "added_first"
    ADDED_LAST = "added_last"
    ALPHABETICAL = "alphabetical"
    ALPHABETICAL_DESC = "alphabetical_desc"
    ARRANGED = "arranged"
    COMMENTS = "comments"
    LIKES = "likes"
    MODIFIED_TIME_ASC = "modified_time_asc"
    MODIFIED_TIME_DESC = "modified_time_desc"
    NEWEST = "newest"
    OLDEST = "oldest"
    PLAYS = "plays"

    __str__ = str.__str__


Sort19OrStr: TypeAlias = Annotated[Sort19 | str, open_enum_validator(Sort19)]
