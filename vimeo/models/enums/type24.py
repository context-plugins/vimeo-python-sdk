from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type24(str, Enum):
    """The type of payment method.

    Option descriptions:
     * ``PAYMENT_METHOD_TYPES_APPLEPAY`` - The payment method is Apple Pay.
     * ``PAYMENT_METHOD_TYPES_BANK_ACCOUNT`` - The payment method is a bank account.
     * ``PAYMENT_METHOD_TYPES_CARD`` - The payment method is a card.
     * ``PAYMENT_METHOD_TYPES_CC_REF`` - The payment method is a credit card reference.
     * ``PAYMENT_METHOD_TYPES_GOOGLEPAY`` - The payment method is Google Pay.
     * ``PAYMENT_METHOD_TYPES_PAYPAL`` - The payment method is a PayPal account.
     * ``PAYMENT_METHOD_TYPES_TYPES_UNSPECIFIED`` - The payment method type is unspecified."""

    PAYMENT_METHOD_TYPES_APPLEPAY = "PAYMENT_METHOD_TYPES_APPLEPAY"
    PAYMENT_METHOD_TYPES_BANK_ACCOUNT = "PAYMENT_METHOD_TYPES_BANK_ACCOUNT"
    PAYMENT_METHOD_TYPES_CARD = "PAYMENT_METHOD_TYPES_CARD"
    PAYMENT_METHOD_TYPES_CC_REF = "PAYMENT_METHOD_TYPES_CC_REF"
    PAYMENT_METHOD_TYPES_GOOGLEPAY = "PAYMENT_METHOD_TYPES_GOOGLEPAY"
    PAYMENT_METHOD_TYPES_PAYPAL = "PAYMENT_METHOD_TYPES_PAYPAL"
    PAYMENT_METHOD_TYPES_TYPES_UNSPECIFIED = "PAYMENT_METHOD_TYPES_TYPES_UNSPECIFIED"

    __str__ = str.__str__


Type24OrStr: TypeAlias = Annotated[Type24 | str, open_enum_validator(Type24)]
