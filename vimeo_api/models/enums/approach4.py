from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Approach4(str, Enum):
    """The approach by which to upload the version.

    Option descriptions:
     * ``post`` - Use the POST approach.
     * ``pull`` - Use the pull approach.
     * ``tus`` - Use the tus approach."""

    POST = "post"
    PULL = "pull"
    TUS = "tus"

    __str__ = str.__str__


Approach4OrStr: TypeAlias = Annotated[Approach4 | str, open_enum_validator(Approach4)]
