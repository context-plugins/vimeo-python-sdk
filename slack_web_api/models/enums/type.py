from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type(str, Enum):
    TEXT = "text"
    DATE = "date"
    LINK = "link"
    MAILTO = "mailto"
    OPTIONS_LIST = "options_list"
    USER = "user"

    __str__ = str.__str__


TypeOrStr: TypeAlias = Annotated[Type | str, open_enum_validator(Type)]
