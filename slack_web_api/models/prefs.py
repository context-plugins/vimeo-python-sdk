from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Prefs(SdkBaseModel):
    channels: list[str]
    groups: list[str]


class PrefsDict(TypedDict):
    channels: list[str]
    groups: list[str]
