from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class OndemandPagesRegionsRequest(SdkBaseModel):
    countries: Optional[list[str]] = UNSET
    """An array of country codes for the regions to remove."""


class OndemandPagesRegionsRequestDict(TypedDict):
    countries: NotRequired[list[str]]
