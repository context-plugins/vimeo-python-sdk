from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel
from .profile1 import Profile1, Profile1Dict


class UsersSetPhotoschema(SdkBaseModel):
    """Schema for successful response from users.setPhoto method"""

    ok: Literal["True"] = "True"
    profile: Profile1


class UsersSetPhotoschemaDict(TypedDict):
    ok: NotRequired[Literal["True"]]
    profile: Profile1 | Profile1Dict
