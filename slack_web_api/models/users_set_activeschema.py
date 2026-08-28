from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class UsersSetActiveschema(SdkBaseModel):
    """Schema for successful response from users.setActive method"""

    ok: Literal["True"] = "True"


class UsersSetActiveschemaDict(TypedDict):
    ok: NotRequired[Literal["True"]]
