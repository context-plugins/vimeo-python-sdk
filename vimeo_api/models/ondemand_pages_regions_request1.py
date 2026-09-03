from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class OndemandPagesRegionsRequest1(SdkBaseModel):
    countries: list[str]
    """An array of country codes for the regions to add."""


class OndemandPagesRegionsRequest1Dict(TypedDict):
    countries: list[str]
