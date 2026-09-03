from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Showing(str, Enum):
    """The type of quota for the values of the **upload_quota.space** field.

    Option descriptions:
     * ``lifetime`` - The quota type is lifetime.
     * ``periodic`` - The quota type is periodic."""

    LIFETIME = "lifetime"
    PERIODIC = "periodic"

    __str__ = str.__str__


ShowingOrStr: TypeAlias = Annotated[Showing | str, open_enum_validator(Showing)]
