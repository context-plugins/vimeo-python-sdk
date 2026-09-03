from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AccessType1(str, Enum):
    """The promotion access type, which is a purchase option that isn't available in the On Demand container. Use the
    **download** and **stream_period** parameters to define additional characteristics for the ``vip`` type.

    Option descriptions:
     * ``default`` - The promotion grants a discount on the existing purchase options for an On Demand container.
     * ``vip`` - The promotion grants free access to On Demand content before it's released."""

    DEFAULT = "default"
    VIP = "vip"

    __str__ = str.__str__


AccessType1OrStr: TypeAlias = Annotated[AccessType1 | str, open_enum_validator(AccessType1)]
