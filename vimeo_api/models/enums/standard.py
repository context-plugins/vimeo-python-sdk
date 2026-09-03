from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Standard(str, Enum):
    AICC = "aicc"
    CMI5 = "cmi5"
    SCORM12 = "scorm12"
    SCORM2004_3RD = "scorm2004_3rd"
    TINCAN = "tincan"

    __str__ = str.__str__


StandardOrStr: TypeAlias = Annotated[Standard | str, open_enum_validator(Standard)]
