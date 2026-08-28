from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .embed16 import Embed16, Embed16Dict


class MePresetsRequest(SdkBaseModel):
    apply_to_all: Optional[bool] = UNSET
    """Whether to apply the preset to all of the user's videos."""

    embed: Optional[Embed16] = UNSET
    name: Optional[str] = UNSET
    """The name of the embed preset."""


class MePresetsRequestDict(TypedDict):
    apply_to_all: NotRequired[bool]
    embed: NotRequired[Embed16 | Embed16Dict]
    name: NotRequired[str]
