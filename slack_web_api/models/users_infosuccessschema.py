from __future__ import annotations

from typing import Any, Literal

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class UsersInfosuccessschema(SdkBaseModel):
    """Schema for successful response from users.info method"""

    ok: Literal["True"] = "True"
    user: Any


class UsersInfosuccessschemaDict(TypedDict):
    ok: NotRequired[Literal["True"]]
    user: Any
