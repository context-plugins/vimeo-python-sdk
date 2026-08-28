from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Scopes(SdkBaseModel):
    app_home: Optional[list[str]] = UNSET
    channel: Optional[list[str]] = UNSET
    group: Optional[list[str]] = UNSET
    im: Optional[list[str]] = UNSET
    mpim: Optional[list[str]] = UNSET
    team: Optional[list[str]] = UNSET
    user: Optional[list[str]] = UNSET


class ScopesDict(TypedDict):
    app_home: NotRequired[list[str]]
    channel: NotRequired[list[str]]
    group: NotRequired[list[str]]
    im: NotRequired[list[str]]
    mpim: NotRequired[list[str]]
    team: NotRequired[list[str]]
    user: NotRequired[list[str]]
