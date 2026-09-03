from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AgeVerificationStatus(str, Enum):
    """The status of the user's age verification.

    Option descriptions:
     * ``failed`` - The user has failed age verification.
     * ``passed`` - The user has passed age verification.
     * ``pending`` - The user's age verification is pending."""

    FAILED = "failed"
    PASSED = "passed"
    PENDING = "pending"

    __str__ = str.__str__


AgeVerificationStatusOrStr: TypeAlias = Annotated[
    AgeVerificationStatus | str, open_enum_validator(AgeVerificationStatus)
]
