from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .reason2 import Reason2, Reason2Dict


class Disabled3(SdkBaseModel):
    """Whether the publish-to-social feature is disabled."""

    enable_link: Optional[str] = UNSET
    """The link to re-enable the publish-to-social feature."""

    reasons: Optional[list[Reason2]] = UNSET
    """The reasons why publish-to-social presets are disabled for the video."""


class Disabled3Dict(TypedDict):
    enable_link: NotRequired[str]
    reasons: NotRequired[list[Reason2 | Reason2Dict]]
