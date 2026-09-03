from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Status17(str, Enum):
    """The purchase status of the product.

    Option descriptions:
     * ``available`` - The product is available for purchase.
     * ``purchased`` - The product is already purchased.
     * ``unavailable`` - The product isn't available for purchase."""

    AVAILABLE = "available"
    PURCHASED = "purchased"
    UNAVAILABLE = "unavailable"

    __str__ = str.__str__


Status17OrStr: TypeAlias = Annotated[Status17 | str, open_enum_validator(Status17)]
