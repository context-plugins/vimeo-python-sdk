from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Filter8(str, Enum):
    NOT_IN_FOLDER = "not_in_folder"
    NOT_IN_SHOWCASE = "not_in_showcase"

    __str__ = str.__str__


Filter8OrStr: TypeAlias = Annotated[Filter8 | str, open_enum_validator(Filter8)]
