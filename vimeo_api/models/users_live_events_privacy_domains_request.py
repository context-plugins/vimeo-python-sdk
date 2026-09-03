from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class UsersLiveEventsPrivacyDomainsRequest(SdkBaseModel):
    allowed_domains: Optional[list[str]] = UNSET
    """An array of the domains on which the embedded event can appear."""


class UsersLiveEventsPrivacyDomainsRequestDict(TypedDict):
    allowed_domains: NotRequired[list[str]]
