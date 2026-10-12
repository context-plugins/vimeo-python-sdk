from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Status14(int, Enum):
    """The ingest status of the live video.

    Option descriptions:
     * ``0`` - There’s a live video, but no RMTP URL or key.
     * ``1`` - There’s an RMTP URL and key, but the machine is provisioning.
     * ``2`` - There’s an RMTP URL and key, and the machine is provisioned, but the stream hasn’t started yet.
     * ``3`` - There’s an RMTP URL and key, and the machine is provisioned, but the stream didn’t start before the
            machine timed out.
     * ``4`` - The stream has started and is currently underway.
     * ``5`` - The stream has ended."""

    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5

    __str__ = str.__str__


Status14OrInt: TypeAlias = Annotated[Status14 | int, open_enum_validator(Status14)]
