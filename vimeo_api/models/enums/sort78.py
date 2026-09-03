from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Sort78(str, Enum):
    DEFAULT = "default"

    __str__ = str.__str__


Sort78OrStr: TypeAlias = Annotated[Sort78 | str, open_enum_validator(Sort78)]
