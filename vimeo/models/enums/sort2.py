from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Sort2(str, Enum):
    ALPHABETICAL = "alphabetical"
    COMMENTS = "comments"
    DATE = "date"
    DEFAULT = "default"
    DURATION = "duration"
    LAST_USER_ACTION_EVENT_DATE = "last_user_action_event_date"
    LIKES = "likes"
    MODIFIED_TIME = "modified_time"
    PLAYS = "plays"

    __str__ = str.__str__


Sort2OrStr: TypeAlias = Annotated[Sort2 | str, open_enum_validator(Sort2)]
