from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type52(str, Enum):
    DUBBING = "dubbing"
    SUBTITLING = "subtitling"
    TRANSCRIPTION = "transcription"

    __str__ = str.__str__


Type52OrStr: TypeAlias = Annotated[Type52 | str, open_enum_validator(Type52)]
