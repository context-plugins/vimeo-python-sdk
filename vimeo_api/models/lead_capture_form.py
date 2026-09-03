from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class LeadCaptureForm(SdkBaseModel):
    """Information about the authenticated user's lead capture form. This data requires a bearer token with the
    ``private`` scope."""

    options: Optional[list[str]] = UNSET
    """An array of HTTP methods permitted on this URI. This data requires a bearer token with the ``private`` scope."""


class LeadCaptureFormDict(TypedDict):
    options: NotRequired[list[str]]
