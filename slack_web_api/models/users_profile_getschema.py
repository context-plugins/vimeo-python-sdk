from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel
from .userprofileobject import Userprofileobject, UserprofileobjectDict


class UsersProfileGetschema(SdkBaseModel):
    """Schema for successful response from users.profile.get method"""

    ok: Literal["True"] = "True"
    profile: Userprofileobject


class UsersProfileGetschemaDict(TypedDict):
    ok: NotRequired[Literal["True"]]
    profile: Userprofileobject | UserprofileobjectDict
