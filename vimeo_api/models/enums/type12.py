from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type12(str, Enum):
    """The type of text decoration.

    Option descriptions:
     * ``url`` - The URL of the Vimeo video."""

    URL = "url"

    __str__ = str.__str__


Type12OrStr: TypeAlias = Annotated[Type12 | str, open_enum_validator(Type12)]
