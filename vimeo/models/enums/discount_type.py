from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class DiscountType(str, Enum):
    """The type of discount that the promotion provides.

    Option descriptions:
     * ``dollars`` - The promotion discounts a fixed amount from the full purchase price.
     * ``free`` - The promotion discounts the full purchase price. When **access_type** is ``vip``, **discount_type** is
            always ``free``.
     * ``percent`` - The promotion discounts a percentage of the full purchase price."""

    DOLLARS = "dollars"
    FREE = "free"
    PERCENT = "percent"

    __str__ = str.__str__


DiscountTypeOrStr: TypeAlias = Annotated[DiscountType | str, open_enum_validator(DiscountType)]
