from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.approach2 import Approach2OrStr


class Upload2(SdkBaseModel):
    approach: Approach2OrStr
    """The upload approach.

    Option descriptions:
     * ``post`` - Use the POST approach.
     * ``pull`` - Use the pull approach.
     * ``tus`` - Use the tus approach."""

    link: Optional[str] = UNSET
    """The public URL at which the video is hosted. The URL must be valid for at least 24 hours. Use this parameter when
    **approach** is ``pull``."""

    redirect_url: Optional[str] = UNSET
    """The app's redirect URL. Use this parameter when **approach** is ``post``."""

    size: Optional[str] = UNSET
    """The size in bytes of the video to upload. The maximum value of this field is ``322122547200``, which corresponds
    to 300 GB."""


class Upload2Dict(TypedDict):
    approach: Approach2OrStr
    link: NotRequired[str]
    redirect_url: NotRequired[str]
    size: NotRequired[str]
