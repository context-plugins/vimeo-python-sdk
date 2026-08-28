from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Brand(str, Enum):
    """The brand of the card.

    Option descriptions:
     * ``CARD_BRAND_AMERICAN_EXPRESS`` - The card brand is American Express.
     * ``CARD_BRAND_DISCOVER`` - The card brand is Discover.
     * ``CARD_BRAND_JCB`` - The card brand is JCB.
     * ``CARD_BRAND_MASTER_CARD`` - The card brand is Mastercard.
     * ``CARD_BRAND_UNION_PAY`` - The card brand is UnionPay.
     * ``CARD_BRAND_UNSPECIFIED`` - The card brand is unspecified.
     * ``CARD_BRAND_VISA`` - The card brand is Visa."""

    CARD_BRAND_AMERICAN_EXPRESS = "CARD_BRAND_AMERICAN_EXPRESS"
    CARD_BRAND_DISCOVER = "CARD_BRAND_DISCOVER"
    CARD_BRAND_JCB = "CARD_BRAND_JCB"
    CARD_BRAND_MASTER_CARD = "CARD_BRAND_MASTER_CARD"
    CARD_BRAND_UNION_PAY = "CARD_BRAND_UNION_PAY"
    CARD_BRAND_UNSPECIFIED = "CARD_BRAND_UNSPECIFIED"
    CARD_BRAND_VISA = "CARD_BRAND_VISA"

    __str__ = str.__str__


BrandOrStr: TypeAlias = Annotated[Brand | str, open_enum_validator(Brand)]
