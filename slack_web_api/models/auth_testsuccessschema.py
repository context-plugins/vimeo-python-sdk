from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class AuthTestsuccessschema(SdkBaseModel):
    """Schema for successful response auth.test method"""

    bot_id: Optional[str] = UNSET
    is_enterprise_install: Optional[bool] = UNSET
    ok: Literal["True"] = "True"
    team: str
    team_id: str
    url: str
    user: str
    user_id: str


class AuthTestsuccessschemaDict(TypedDict):
    bot_id: NotRequired[str]
    is_enterprise_install: NotRequired[bool]
    ok: NotRequired[Literal["True"]]
    team: str
    team_id: str
    url: str
    user: str
    user_id: str
