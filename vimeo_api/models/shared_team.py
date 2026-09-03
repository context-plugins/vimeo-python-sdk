from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class SharedTeam(SdkBaseModel):
    """Information about the team of the shared item."""

    link: Optional[str] = UNSET
    """The absolute URL of the authenticated users's profile page."""

    logo_url: OptionalNullable[str] = UNSET
    """The team logo URL."""

    name: Optional[str] = UNSET
    """The display name of the team of the shared item."""

    uri: Optional[str] = UNSET
    """The unique identifier to access the team owner user resource."""


class SharedTeamDict(TypedDict):
    link: NotRequired[str]
    logo_url: NotRequired[str | None]
    name: NotRequired[str]
    uri: NotRequired[str]
