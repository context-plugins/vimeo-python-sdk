from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class QueryFields(str, Enum):
    CHAPTERS = "chapters"
    DESCRIPTION = "description"
    TAGS = "tags"
    TITLE = "title"

    __str__ = str.__str__


QueryFieldsOrStr: TypeAlias = Annotated[QueryFields | str, open_enum_validator(QueryFields)]
