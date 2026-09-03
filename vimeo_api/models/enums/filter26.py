from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Filter26(str, Enum):
    BATCH = "batch"
    DEFAULT = "default"
    SINGLE = "single"
    VIP = "vip"

    __str__ = str.__str__


Filter26OrStr: TypeAlias = Annotated[Filter26 | str, open_enum_validator(Filter26)]
