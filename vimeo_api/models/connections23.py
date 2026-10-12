from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .shared_team import SharedTeam, SharedTeamDict
from .shared_user import SharedUser, SharedUserDict


class Connections23(SdkBaseModel):
    """A list of resource URIs related to the item."""

    shared_team: OptionalNullable[SharedTeam] = UNSET
    """Information about the team of the shared item."""

    shared_user: OptionalNullable[SharedUser] = UNSET
    """Information about the user who shared the item."""


class Connections23Dict(TypedDict):
    shared_team: NotRequired[SharedTeamDict | None]
    shared_user: NotRequired[SharedUserDict | None]
