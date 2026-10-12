from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .videos4 import Videos4, Videos4Dict


class Preferences(SdkBaseModel):
    videos: Videos4


class PreferencesDict(TypedDict):
    videos: Videos4Dict
