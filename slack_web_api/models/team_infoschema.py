from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel
from .team_object import TeamObject, TeamObjectDict


class TeamInfoschema(SdkBaseModel):
    """Schema for successful response from team.info method"""

    ok: Literal["True"] = "True"
    team: TeamObject


class TeamInfoschemaDict(TypedDict):
    ok: NotRequired[Literal["True"]]
    team: TeamObject | TeamObjectDict
