from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ApimethodusersGetPresence(SdkBaseModel):
    """Generated from users.getPresence with shasum e7251aec575d8863f9e0eb38663ae9dc26655f65"""

    auto_away: Optional[bool] = UNSET
    connection_count: Optional[int] = UNSET
    last_activity: Optional[int] = UNSET
    manual_away: Optional[bool] = UNSET
    ok: Literal["True"] = "True"
    online: Optional[bool] = UNSET
    presence: str


class ApimethodusersGetPresenceDict(TypedDict):
    auto_away: NotRequired[bool]
    connection_count: NotRequired[int]
    last_activity: NotRequired[int]
    manual_away: NotRequired[bool]
    ok: NotRequired[Literal["True"]]
    online: NotRequired[bool]
    presence: str
