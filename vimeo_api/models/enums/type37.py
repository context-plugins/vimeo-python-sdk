from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type37(str, Enum):
    """The type of the promotion. When **access_type** is ``vip``, the value for this parameter must be ``batch``.

    Option descriptions:
     * ``batch`` - The promotion type that generates many random codes to use one time each.
     * ``single`` - The promotion type that generates one code to use many times."""

    BATCH = "batch"
    SINGLE = "single"

    __str__ = str.__str__


Type37OrStr: TypeAlias = Annotated[Type37 | str, open_enum_validator(Type37)]
