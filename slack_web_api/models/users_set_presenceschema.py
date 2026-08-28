from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class UsersSetPresenceschema(SdkBaseModel):
    """Schema for successful response from users.setPresence method"""

    ok: Literal["True"] = "True"


class UsersSetPresenceschemaDict(TypedDict):
    ok: NotRequired[Literal["True"]]
