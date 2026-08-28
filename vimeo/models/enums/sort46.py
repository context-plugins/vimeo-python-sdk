from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Sort46(str, Enum):
    ALPHABETICAL = "alphabetical"
    DATE = "date"
    DEFAULT = "default"
    DURATION = "duration"
    FOLDER_PATH = "folder_path"
    LAST_USER_ACTION_EVENT_DATE = "last_user_action_event_date"

    __str__ = str.__str__


Sort46OrStr: TypeAlias = Annotated[Sort46 | str, open_enum_validator(Sort46)]
