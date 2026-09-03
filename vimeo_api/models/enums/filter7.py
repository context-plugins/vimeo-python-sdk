from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Filter7(str, Enum):
    AUDIOTRACKS = "audiotracks"
    TEXTTRACKS = "texttracks"

    __str__ = str.__str__


Filter7OrStr: TypeAlias = Annotated[Filter7 | str, open_enum_validator(Filter7)]
