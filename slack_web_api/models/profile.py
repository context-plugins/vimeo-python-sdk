from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .objs_team_profile_field import ObjsTeamProfileField, ObjsTeamProfileFieldDict


class Profile(SdkBaseModel):
    fields: list[ObjsTeamProfileField]


class ProfileDict(TypedDict):
    fields: list[ObjsTeamProfileField | ObjsTeamProfileFieldDict]
