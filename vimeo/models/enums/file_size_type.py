from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class FileSizeType(str, Enum):
    """The status of the video and its corresponding file size type.

    Option descriptions:
     * ``PROCESSING`` - The video is still processing or transcoding, and its file size isn't available yet.
     * ``QUOTA_EXEMPT_CLIP`` - The video is exempt from the user's storage quota.
     * ``QUOTA_EXEMPT_USER`` - The user is on an unlimited plan, and the video doesn't count against their storage
            quota.
     * ``STOCK`` - The video is stock footage. Stock videos don't count against the user's storage quota.
     * ``UPLOAD`` - The video is a regular upload, and its file size counts against the user's storage quota.
     * ``UPLOAD_FAILURE`` - The video failed to upload, and its file size doesn't count against the user's storage
            quota.
     * ``VIMEO_CREATE`` - The video was created using the Vimeo Create app. Vimeo Create videos don't count against the
            user's storage quota.
     * ``VIMEO_RECORD`` - The video was recorded using the Vimeo Record app. Videos for some Vimeo Record API apps don't
            count against the user's storage quota."""

    PROCESSING = "PROCESSING"
    QUOTA_EXEMPT_CLIP = "QUOTA_EXEMPT_CLIP"
    QUOTA_EXEMPT_USER = "QUOTA_EXEMPT_USER"
    STOCK = "STOCK"
    UPLOAD = "UPLOAD"
    UPLOAD_FAILURE = "UPLOAD_FAILURE"
    VIMEO_CREATE = "VIMEO_CREATE"
    VIMEO_RECORD = "VIMEO_RECORD"

    __str__ = str.__str__


FileSizeTypeOrStr: TypeAlias = Annotated[FileSizeType | str, open_enum_validator(FileSizeType)]
