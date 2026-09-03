from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ExplicitAccessSummary(SdkBaseModel):
    """The explicit access summary of the video. This data requires a bearer token with the ``private`` scope."""

    all_team_count: Optional[float] = UNSET
    """The number of direct access grants for all teams. This data requires a bearer token with the ``private``
    scope."""

    team_group_count: Optional[float] = UNSET
    """The number of direct access grants for team groups. This data requires a bearer token with the ``private``
    scope."""

    team_user_count: Optional[float] = UNSET
    """The number of direct access grants for team users. This data requires a bearer token with the ``private``
    scope."""


class ExplicitAccessSummaryDict(TypedDict):
    all_team_count: NotRequired[float]
    team_group_count: NotRequired[float]
    team_user_count: NotRequired[float]
