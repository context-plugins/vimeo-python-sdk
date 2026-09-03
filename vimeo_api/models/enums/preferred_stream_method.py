from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PreferredStreamMethod(str, Enum):
    """The preferred streaming method.

    Option descriptions:
     * ``browser`` - Stream in the browser.
     * ``encoder`` - Stream by the encoder."""

    BROWSER = "browser"
    ENCODER = "encoder"

    __str__ = str.__str__


PreferredStreamMethodOrStr: TypeAlias = Annotated[
    PreferredStreamMethod | str, open_enum_validator(PreferredStreamMethod)
]
