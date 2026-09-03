from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Uri(SdkBaseModel):
    """The redirect URIs associated with the plan."""

    annual: str | None
    """The redirect URI for the annual plan in the user's cart."""

    free_trial: str | None
    """The redirect URI for the free trial in the user's cart."""

    monthly: str | None
    """The redirect URI for the monthly plan in the user's cart."""


class UriDict(TypedDict):
    annual: str | None
    free_trial: str | None
    monthly: str | None
