from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type(str, Enum):
    """The type of picture.

    Option descriptions:
     * ``caution`` - The picture isn't appropriate for all ages.
     * ``custom`` - The picture is a custom video image.
     * ``default`` - The picture is the default video image."""

    CAUTION = "caution"
    CUSTOM = "custom"
    DEFAULT = "default"

    __str__ = str.__str__


TypeOrStr: TypeAlias = Annotated[Type | str, open_enum_validator(Type)]
