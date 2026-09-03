from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Filter(str, Enum):
    CONDITIONAL_FEATURED = "conditional_featured"
    EMBEDDABLE = "embeddable"

    __str__ = str.__str__


FilterOrStr: TypeAlias = Annotated[Filter | str, open_enum_validator(Filter)]
