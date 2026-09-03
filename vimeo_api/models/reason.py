from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.icon import IconOrStr


class Reason(SdkBaseModel):
    icon: Optional[IconOrStr] = UNSET
    """An icon that represents the reason why showcase presets are disabled. This data requires a bearer token with the
    ``private`` scope.

    Option descriptions:
     * ``clock`` - The reason is represented by a clock icon.
     * ``create`` - The reason is represented by a create icon.
     * ``image`` - The reason is represented by an image icon.
     * ``theme`` - The reason is represented by a theme icon."""

    message: Optional[str] = UNSET
    """An explanation for the user about why showcase presets are disabled. This data requires a bearer token with the
    ``private`` scope."""


class ReasonDict(TypedDict):
    icon: NotRequired[IconOrStr]
    message: NotRequired[str]
