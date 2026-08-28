from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.icon1 import Icon1OrStr


class Reason1(SdkBaseModel):
    icon: Optional[Icon1OrStr] = UNSET
    """An icon that represents the reason why available showcase presets are disabled. This data requires a bearer token
    with the ``private`` scope.

    Option descriptions:
     * ``clock`` - The reason is represented by a clock icon.
     * ``create`` - The reason is represented by a create icon.
     * ``image`` - The reason is represented by an image icon.
     * ``theme`` - The reason is represented by a theme icon."""

    message: Optional[str] = UNSET
    """An explanation for the user about why available showcase presets are disabled. This data requires a bearer token
    with the ``private`` scope."""


class Reason1Dict(TypedDict):
    icon: NotRequired[Icon1OrStr]
    message: NotRequired[str]
