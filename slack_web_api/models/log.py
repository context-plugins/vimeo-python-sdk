from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Log(SdkBaseModel):
    admin_app_id: Optional[str] = UNSET
    app_id: str
    app_type: str
    change_type: str
    channel: Optional[str] = UNSET
    date: str
    scope: str
    service_id: Optional[str] = UNSET
    service_type: Optional[str] = UNSET
    user_id: str
    user_name: str


class LogDict(TypedDict):
    admin_app_id: NotRequired[str]
    app_id: str
    app_type: str
    change_type: str
    channel: NotRequired[str]
    date: str
    scope: str
    service_id: NotRequired[str]
    service_type: NotRequired[str]
    user_id: str
    user_name: str
