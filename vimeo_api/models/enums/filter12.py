from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Filter12(str, Enum):
    MODERATED = "moderated"

    __str__ = str.__str__


Filter12OrStr: TypeAlias = Annotated[Filter12 | str, open_enum_validator(Filter12)]
