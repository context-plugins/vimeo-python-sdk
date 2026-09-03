from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Latency2(str, Enum):
    """The type of stream delay on the viewer side.

    Option descriptions:
     * ``fail-safe`` - The latency is in the failsafe range, with a delay of 60-75 seconds.
     * ``low`` - The latency is low, with a delay of 5-7 seconds.
     * ``standard`` - The latency is standard, with a delay of 15-20 seconds."""

    FAIL_SAFE = "fail-safe"
    LOW = "low"
    STANDARD = "standard"

    __str__ = str.__str__


Latency2OrStr: TypeAlias = Annotated[Latency2 | str, open_enum_validator(Latency2)]
