from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Sort39(str, Enum):
    ALPHABETICAL = "alphabetical"
    DATE = "date"
    DEFAULT = "default"
    DURATION = "duration"
    LAST_USER_ACTION_EVENT_DATE = "last_user_action_event_date"
    LIKES = "likes"
    MODIFIED_TIME = "modified_time"
    PLAYS = "plays"

    __str__ = str.__str__


Sort39OrStr: TypeAlias = Annotated[Sort39 | str, open_enum_validator(Sort39)]
