from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type13(str, Enum):
    """The data type of the metadata field.

    Option descriptions:
     * ``bool`` - Boolean value.
     * ``date`` - Date value.
     * ``int`` - Integer value.
     * ``multi-select`` - Multi-select from allowed values.
     * ``select`` - Single-select from allowed values.
     * ``str`` - String value."""

    BOOL = "bool"
    DATE = "date"
    INT = "int"
    MULTI_SELECT = "multi-select"
    SELECT = "select"
    STR = "str"

    __str__ = str.__str__


Type13OrStr: TypeAlias = Annotated[Type13 | str, open_enum_validator(Type13)]
