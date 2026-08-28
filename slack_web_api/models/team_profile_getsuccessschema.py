from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel
from .profile import Profile, ProfileDict


class TeamProfileGetsuccessschema(SdkBaseModel):
    """Schema for successful response from team.profile.get method"""

    ok: Literal["True"] = "True"
    profile: Profile


class TeamProfileGetsuccessschemaDict(TypedDict):
    ok: NotRequired[Literal["True"]]
    profile: Profile | ProfileDict
