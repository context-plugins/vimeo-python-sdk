from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Balance(SdkBaseModel):
    expiration_date: Optional[str] = UNSET
    """The expiration date of the balance in ISO 8601 format."""

    remaining: Optional[float] = UNSET
    """The number of AI credits that are remaining for the balance."""


class BalanceDict(TypedDict):
    expiration_date: NotRequired[str]
    remaining: NotRequired[float]
