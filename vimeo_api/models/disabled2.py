from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .reason1 import Reason1, Reason1Dict


class Disabled2(SdkBaseModel):
    enable_link: Optional[str] = UNSET
    """The link to re-enable the available showcase presets feature. This data requires a bearer token with the
    ``private`` scope."""

    reasons: Optional[list[Reason1]] = UNSET
    """The reasons why available showcase presets are disabled for the video. This data requires a bearer token with the
    ``private`` scope."""


class Disabled2Dict(TypedDict):
    enable_link: NotRequired[str]
    reasons: NotRequired[list[Reason1Dict]]
