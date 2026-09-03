from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Error2(str, Enum):
    """The error that caused the upload to fail.

    Option descriptions:
     * ``analysis_failed`` - The uploaded file could not be decoded.
     * ``disallowed_address`` - The URL for a 'pull' approach upload resolved to a disallowed address.
     * ``disallowed_content_type`` - The user attempted to upload a file of an unsupported Content-Type.
     * ``duration_too_long`` - The uploaded video exceeds the maximum allowed duration of 24 hours.
     * ``duration_too_short`` - The uploaded video is shorter than the minimum allowed duration of 0.5 seconds.
     * ``empty_upload`` - The user attempted to upload a 0-byte file.
     * ``exceeded_retry_count`` - The upload failed too many times with otherwise retryable errors.
     * ``internal`` - The upload failed due to an internal error.
     * ``invalid_redirects`` - The URL for a 'pull' upload performed too many redirects.
     * ``max_file_size_exceeded`` - The uploaded file exceeds the maximum allowed size of 300 GB.
     * ``missing_video_stream`` - The uploaded file contains no video stream.
     * ``remote_bad_request`` - The remote server for a 'pull'-approach upload responded with another 400-level status
            error.
     * ``remote_forbidden`` - The remote server for a 'pull'-approach upload responded with a 'Forbidden' error.
     * ``remote_internal`` - The remote server for a 'pull'-approach upload responded with a 500-level status error.
     * ``remote_not_found`` - The remote server for a 'pull'-approach upload responded with a 'Not Found' error.
     * ``remote_unauthorized`` - The remote server for a 'pull'-approach upload responded with an 'Unauthorized' error.
     * ``resolution_dimension_too_small`` - The uploaded video's resolution has a dimension under the minimum allowed
            value of 2 pixels.
     * ``unsupported_video_projection`` - The uploaded video uses an unsupported spatial projection."""

    ANALYSIS_FAILED = "analysis_failed"
    DISALLOWED_ADDRESS = "disallowed_address"
    DISALLOWED_CONTENT_TYPE = "disallowed_content_type"
    DURATION_TOO_LONG = "duration_too_long"
    DURATION_TOO_SHORT = "duration_too_short"
    EMPTY_UPLOAD = "empty_upload"
    EXCEEDED_RETRY_COUNT = "exceeded_retry_count"
    INTERNAL = "internal"
    INVALID_REDIRECTS = "invalid_redirects"
    MAX_FILE_SIZE_EXCEEDED = "max_file_size_exceeded"
    MISSING_VIDEO_STREAM = "missing_video_stream"
    REMOTE_BAD_REQUEST = "remote_bad_request"
    REMOTE_FORBIDDEN = "remote_forbidden"
    REMOTE_INTERNAL = "remote_internal"
    REMOTE_NOT_FOUND = "remote_not_found"
    REMOTE_UNAUTHORIZED = "remote_unauthorized"
    RESOLUTION_DIMENSION_TOO_SMALL = "resolution_dimension_too_small"
    UNSUPPORTED_VIDEO_PROJECTION = "unsupported_video_projection"

    __str__ = str.__str__


Error2OrStr: TypeAlias = Annotated[Error2 | str, open_enum_validator(Error2)]
