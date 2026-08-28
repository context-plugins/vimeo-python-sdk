from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Sort37(str, Enum):
    ALPHABETICAL = "alphabetical"
    DATE = "date"
    DEFAULT = "default"
    DURATION = "duration"
    LAST_USER_ACTION_EVENT_DATE = "last_user_action_event_date"

    __str__ = str.__str__


Sort37OrStr: TypeAlias = Annotated[Sort37 | str, open_enum_validator(Sort37)]
