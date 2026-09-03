from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ScoringAlgorithm(str, Enum):
    PASSFAIL = "passfail"
    PERCENTAGE = "percentage"
    QUIZ = "quiz"

    __str__ = str.__str__


ScoringAlgorithmOrStr: TypeAlias = Annotated[ScoringAlgorithm | str, open_enum_validator(ScoringAlgorithm)]
