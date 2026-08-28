from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Id(SdkBaseModel):
    """The SKUs of the plans."""

    annual: str | None
    """The SKU of the annual plan."""

    monthly: str | None
    """The SKU of the monthly plan."""


class IdDict(TypedDict):
    annual: str | None
    monthly: str | None
