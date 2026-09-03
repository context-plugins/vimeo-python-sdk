from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Filter2(str, Enum):
    MODERATORS = "moderators"

    __str__ = str.__str__


Filter2OrStr: TypeAlias = Annotated[Filter2 | str, open_enum_validator(Filter2)]
