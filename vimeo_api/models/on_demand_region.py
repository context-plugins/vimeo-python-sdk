from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class OnDemandRegion(SdkBaseModel):
    country_code: str
    """The ISO 3166-1 alpha-2 code for this country."""

    country_name: str
    """The descriptive name of this country."""

    uri: str
    """The region container's relative URI."""


class OnDemandRegionDict(TypedDict):
    country_code: str
    country_name: str
    uri: str
