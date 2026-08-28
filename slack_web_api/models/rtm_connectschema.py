from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel
from .self_model import SelfModel, SelfModelDict
from .team1 import Team1, Team1Dict


class RtmConnectschema(SdkBaseModel):
    """Schema for successful response from rtm.connect method"""

    ok: Literal["True"] = "True"
    self: SelfModel
    team: Team1
    url: str


class RtmConnectschemaDict(TypedDict):
    ok: NotRequired[Literal["True"]]
    self: SelfModel | SelfModelDict
    team: Team1 | Team1Dict
    url: str
