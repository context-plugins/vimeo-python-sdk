from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.status17 import Status17OrStr
from .uri import Uri, UriDict


class Purchase(SdkBaseModel):
    status: Status17OrStr
    """The purchase status of the product.

    Option descriptions:
     * ``available`` - The product is available for purchase.
     * ``purchased`` - The product is already purchased.
     * ``unavailable`` - The product isn't available for purchase."""

    uri: Uri
    """The redirect URIs associated with the plan."""


class PurchaseDict(TypedDict):
    status: Status17OrStr
    uri: Uri | UriDict
