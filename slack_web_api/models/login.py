from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Login(SdkBaseModel):
    count: int
    country: str | None
    date_first: int
    date_last: int
    ip: str | None
    isp: str | None
    region: str | None
    user_agent: str
    user_id: str
    username: str


class LoginDict(TypedDict):
    count: int
    country: str | None
    date_first: int
    date_last: int
    ip: str | None
    isp: str | None
    region: str | None
    user_agent: str
    user_id: str
    username: str
