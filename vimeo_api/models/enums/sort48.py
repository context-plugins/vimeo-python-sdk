from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Sort48(str, Enum):
    MODIFIED_ASC = "modified_asc"
    MODIFIED_DESC = "modified_desc"
    TITLE_ASC = "title_asc"
    TITLE_DESC = "title_desc"

    __str__ = str.__str__


Sort48OrStr: TypeAlias = Annotated[Sort48 | str, open_enum_validator(Sort48)]
