from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.approach4 import Approach4OrStr


class Upload4(SdkBaseModel):
    approach: Approach4OrStr
    """The approach by which to upload the version.

    Option descriptions:
     * ``post`` - Use the POST approach.
     * ``pull`` - Use the pull approach.
     * ``tus`` - Use the tus approach."""

    link: Optional[str] = UNSET
    """The public URL from which to download the version when **upload.approach** is ``pull``. This URL must be valid
    for at least 24 hours."""

    redirect_url: Optional[str] = UNSET
    """The app's redirect URL when **upload.approach** is ``post``."""

    size: Optional[str] = UNSET
    """The upload size of the version."""


class Upload4Dict(TypedDict):
    approach: Approach4OrStr
    link: NotRequired[str]
    redirect_url: NotRequired[str]
    size: NotRequired[str]
