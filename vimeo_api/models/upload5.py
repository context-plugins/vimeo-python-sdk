from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.approach5 import Approach5OrStr


class Upload5(SdkBaseModel):
    approach: Approach5OrStr
    """The type of upload approach. For more information about upload approaches, refer to `Working with Video Uploads
    <https://developer.vimeo.com/api/upload/videos#understanding-upload-approaches>`__.

    Option descriptions:
     * ``post`` - The upload approach is POST.
     * ``pull`` - The upload approach is pull.
     * ``tus`` - The upload approach is tus."""

    link: Optional[str] = UNSET
    """The public URL at which the video is hosted. The URL must be valid for at least 24 hours. Use this parameter when
    **approach** is ``pull``."""

    redirect_url: Optional[str] = UNSET
    """The app's redirect URL. Use this parameter when **approach** is ``post``."""

    size: Optional[str] = UNSET
    """The size in bytes of the asset to upload. The maximum value of this field is ``322122547200``, which corresponds
    to 300 GB."""


class Upload5Dict(TypedDict):
    approach: Approach5OrStr
    link: NotRequired[str]
    redirect_url: NotRequired[str]
    size: NotRequired[str]
