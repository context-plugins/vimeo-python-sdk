from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class BillingAddress(SdkBaseModel):
    """The billing address of the card."""

    address: Optional[str] = UNSET
    """The street address of the billing address."""

    city: Optional[str] = UNSET
    """The city of the billing address."""

    country: Optional[str] = UNSET
    """The country of the billing address."""

    postal_code: Optional[str] = UNSET
    """The postal code of the billing address."""

    state: Optional[str] = UNSET
    """The state of the billing address."""


class BillingAddressDict(TypedDict):
    address: NotRequired[str]
    city: NotRequired[str]
    country: NotRequired[str]
    postal_code: NotRequired[str]
    state: NotRequired[str]
