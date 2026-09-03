from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type48(str, Enum):
    DUBBING = "dubbing"
    SUBTITLING = "subtitling"
    TRANSCRIPTION = "transcription"

    __str__ = str.__str__


Type48OrStr: TypeAlias = Annotated[Type48 | str, open_enum_validator(Type48)]
