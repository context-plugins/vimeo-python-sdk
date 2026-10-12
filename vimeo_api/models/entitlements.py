from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .params import Params, ParamsDict


class Entitlements(SdkBaseModel):
    """The URLs and entitlements of the associated products in the store."""

    id: float | None
    """The entitlement plan ID."""

    params: Params
    """The list of entitlement parameters corresponding to the tier."""


class EntitlementsDict(TypedDict):
    id: float | None
    params: ParamsDict
