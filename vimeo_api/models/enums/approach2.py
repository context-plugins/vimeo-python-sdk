from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Approach2(str, Enum):
    """The upload approach.

    Option descriptions:
     * ``post`` - Use the POST approach.
     * ``pull`` - Use the pull approach.
     * ``tus`` - Use the tus approach."""

    POST = "post"
    PULL = "pull"
    TUS = "tus"

    __str__ = str.__str__


Approach2OrStr: TypeAlias = Annotated[Approach2 | str, open_enum_validator(Approach2)]
