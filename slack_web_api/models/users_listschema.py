from __future__ import annotations

from typing import Any, Literal

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class UsersListschema(SdkBaseModel):
    """Schema for successful response from users.list method"""

    cache_ts: int
    members: list[Any]
    ok: Literal["True"] = "True"
    response_metadata: Optional[Any] = UNSET


class UsersListschemaDict(TypedDict):
    cache_ts: int
    members: list[Any]
    ok: NotRequired[Literal["True"]]
    response_metadata: NotRequired[Any]
