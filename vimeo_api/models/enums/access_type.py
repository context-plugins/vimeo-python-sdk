from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AccessType(str, Enum):
    """The type of access that the promotion grants.

    Option descriptions:
     * ``default`` - The promotion grants discounts on existing product offerings.
     * ``vip`` - The promotion grants free access to On Demand content before it's released, or to access types that
            aren't part of the existing product offerings."""

    DEFAULT = "default"
    VIP = "vip"

    __str__ = str.__str__


AccessTypeOrStr: TypeAlias = Annotated[AccessType | str, open_enum_validator(AccessType)]
