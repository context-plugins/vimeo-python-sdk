from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Current(SdkBaseModel):
    date_started: int
    team_id: str


class CurrentDict(TypedDict):
    date_started: int
    team_id: str
