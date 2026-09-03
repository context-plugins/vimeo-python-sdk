from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class DiscountType1(str, Enum):
    """The type of discount offered by the promotion code. When **access_type** is ``vip``, the value of this parameter
    must be ``free``.

    Option descriptions:
     * ``free`` - The discount reduces the price to zero.
     * ``percent`` - The discount reduces the price by the percentage defined in the **percent_off** parameter."""

    FREE = "free"
    PERCENT = "percent"

    __str__ = str.__str__


DiscountType1OrStr: TypeAlias = Annotated[DiscountType1 | str, open_enum_validator(DiscountType1)]
