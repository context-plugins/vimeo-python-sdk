from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .card1 import Card1, Card1Dict
from .enums.type24 import Type24OrStr


class PaymentMethod(SdkBaseModel):
    account_id: str
    """The ID of the account."""

    card: Optional[Card1] = UNSET
    """Information about the card used to make the payment."""

    created_at: str
    """The time when the payment method was created."""

    disabled_at: str
    """The time when the payment method was disabled."""

    id: str
    """The ID of the payment method."""

    is_default: bool
    """Whether the payment method is the default payment method for the account."""

    type_: Type24OrStr = Field(alias="type")
    """The type of payment method.

    Option descriptions:
     * ``PAYMENT_METHOD_TYPES_APPLEPAY`` - The payment method is Apple Pay.
     * ``PAYMENT_METHOD_TYPES_BANK_ACCOUNT`` - The payment method is a bank account.
     * ``PAYMENT_METHOD_TYPES_CARD`` - The payment method is a card.
     * ``PAYMENT_METHOD_TYPES_CC_REF`` - The payment method is a credit card reference.
     * ``PAYMENT_METHOD_TYPES_GOOGLEPAY`` - The payment method is Google Pay.
     * ``PAYMENT_METHOD_TYPES_PAYPAL`` - The payment method is a PayPal account.
     * ``PAYMENT_METHOD_TYPES_TYPES_UNSPECIFIED`` - The payment method type is unspecified."""

    updated_at: str
    """The time when the payment method was last updated."""


class PaymentMethodDict(TypedDict):
    account_id: str
    card: NotRequired[Card1Dict]
    created_at: str
    disabled_at: str
    id: str
    is_default: bool
    type_: Type24OrStr
    updated_at: str
