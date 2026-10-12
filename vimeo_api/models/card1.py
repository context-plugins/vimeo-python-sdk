from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .billing_address import BillingAddress, BillingAddressDict
from .enums.brand import BrandOrStr


class Card1(SdkBaseModel):
    """Information about the card used to make the payment."""

    billing_address: Optional[BillingAddress] = UNSET
    """The billing address of the card."""

    bin: Optional[str] = UNSET
    """The bank identification number of the card."""

    brand: Optional[BrandOrStr] = UNSET
    """The brand of the card.

    Option descriptions:
     * ``CARD_BRAND_AMERICAN_EXPRESS`` - The card brand is American Express.
     * ``CARD_BRAND_DISCOVER`` - The card brand is Discover.
     * ``CARD_BRAND_JCB`` - The card brand is JCB.
     * ``CARD_BRAND_MASTER_CARD`` - The card brand is Mastercard.
     * ``CARD_BRAND_UNION_PAY`` - The card brand is UnionPay.
     * ``CARD_BRAND_UNSPECIFIED`` - The card brand is unspecified.
     * ``CARD_BRAND_VISA`` - The card brand is Visa."""

    cardholder_name: Optional[str] = UNSET
    """The name of the cardholder."""

    expiration_month: Optional[float] = UNSET
    """The expiration month of the card."""

    expiration_year: Optional[float] = UNSET
    """The expiration year of the card."""

    last_four_digits: Optional[str] = UNSET
    """The last four digits of the card."""


class Card1Dict(TypedDict):
    billing_address: NotRequired[BillingAddressDict]
    bin: NotRequired[str]
    brand: NotRequired[BrandOrStr]
    cardholder_name: NotRequired[str]
    expiration_month: NotRequired[float]
    expiration_year: NotRequired[float]
    last_four_digits: NotRequired[str]
