from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Gender(str, Enum):
    """The authenticated user's gender.

    Option descriptions:
     * ``f`` - The user's preferred pronouns are she and her.
     * ``m`` - The user's preferred pronouns are he and him.
     * ``n`` - The user would rather not give preferred pronouns.
     * ``o`` - The user's preferred pronouns are they and them."""

    F = "f"
    M = "m"
    N = "n"
    O_ = "o"

    __str__ = str.__str__


GenderOrStr: TypeAlias = Annotated[Gender | str, open_enum_validator(Gender)]
