from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.icon2 import Icon2OrStr


class Reason2(SdkBaseModel):
    icon: Optional[Icon2OrStr] = UNSET
    """An icon that represents the reason why publish-to-social presets are disabled.

    Option descriptions:
     * ``clock`` - The reason is represented by a clock icon.
     * ``create`` - The reason is represented by a create icon.
     * ``image`` - The reason is represented by an image icon.
     * ``theme`` - The reason is represented by a theme icon."""

    message: Optional[str] = UNSET
    """An explanation for the user about why publish-to-social presets are disabled."""


class Reason2Dict(TypedDict):
    icon: NotRequired[Icon2OrStr]
    message: NotRequired[str]
