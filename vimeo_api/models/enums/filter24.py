from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Filter24(str, Enum):
    COUNTRY = "country"
    MY_REGION = "my_region"

    __str__ = str.__str__


Filter24OrStr: TypeAlias = Annotated[Filter24 | str, open_enum_validator(Filter24)]
