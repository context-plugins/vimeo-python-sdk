from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type43(str, Enum):
    """The data type of the field. Required when creating a new field. **Immutable** after creation.

    Option descriptions:
     * ``bool`` - Boolean value (``true`` or ``false``).
     * ``date`` - Calendar date in ``YYYY-MM-DD`` format.
     * ``int`` - Integer value.
     * ``multi-select`` - One or more values chosen from the field's ``values`` list.
     * ``select`` - A single value chosen from the field's ``values`` list.
     * ``str`` - Freeform string value."""

    BOOL = "bool"
    DATE = "date"
    INT = "int"
    MULTI_SELECT = "multi-select"
    SELECT = "select"
    STR = "str"

    __str__ = str.__str__


Type43OrStr: TypeAlias = Annotated[Type43 | str, open_enum_validator(Type43)]
