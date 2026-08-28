from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Approach(str, Enum):
    """The approach for uploading the video.

    Option descriptions:
     * ``post`` - The video upload uses the POST approach.
     * ``pull`` - The video upload uses the pull approach.
     * ``tus`` - The video upload uses the tus approach."""

    POST = "post"
    PULL = "pull"
    TUS = "tus"

    __str__ = str.__str__


ApproachOrStr: TypeAlias = Annotated[Approach | str, open_enum_validator(Approach)]
