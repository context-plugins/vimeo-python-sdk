from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Status5(str, Enum):
    """The status code for the availability of the video.

    Option descriptions:
     * ``available`` - The video is available.
     * ``failed`` - There was an error in rendering the video.
     * ``processing`` - Rendering has started and is currently underway for the video.
     * ``quota_exceeded`` - The user's weekly upload quota is exceeded with this video.
     * ``total_cap_exceeded`` - The user's total storage limit is exceeded with this video.
     * ``transcode_starting`` - Transcoding is starting for the video.
     * ``transcoding`` - Transcoding has started and is currently underway for the video.
     * ``transcoding_error`` - There was an error in transcoding the video.
     * ``unavailable`` - The video is unavailable.
     * ``uploading`` - The video is being uploaded.
     * ``uploading_error`` - There was an error in uploading the video."""

    AVAILABLE = "available"
    FAILED = "failed"
    PROCESSING = "processing"
    QUOTA_EXCEEDED = "quota_exceeded"
    TOTAL_CAP_EXCEEDED = "total_cap_exceeded"
    TRANSCODE_STARTING = "transcode_starting"
    TRANSCODING = "transcoding"
    TRANSCODING_ERROR = "transcoding_error"
    UNAVAILABLE = "unavailable"
    UPLOADING = "uploading"
    UPLOADING_ERROR = "uploading_error"

    __str__ = str.__str__


Status5OrStr: TypeAlias = Annotated[Status5 | str, open_enum_validator(Status5)]
