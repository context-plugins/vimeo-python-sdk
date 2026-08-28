from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Status1(str, Enum):
    """The status of the authenticated user's trial.

    Option descriptions:
     * ``free_trial`` - The user is currently in a free trial."""

    FREE_TRIAL = "free_trial"

    __str__ = str.__str__


Status1OrStr: TypeAlias = Annotated[Status1 | str, open_enum_validator(Status1)]
