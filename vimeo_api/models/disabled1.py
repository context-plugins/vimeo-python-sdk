from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .reason import Reason, ReasonDict


class Disabled1(SdkBaseModel):
    enable_link: Optional[str] = UNSET
    """The link to re-enable the showcase presets feature. This data requires a bearer token with the ``private``
    scope."""

    reasons: Optional[list[Reason]] = UNSET
    """The reasons why showcase presets are disabled for the video. This data requires a bearer token with the
    ``private`` scope."""


class Disabled1Dict(TypedDict):
    enable_link: NotRequired[str]
    reasons: NotRequired[list[ReasonDict]]
