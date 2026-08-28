from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.approach import ApproachOrStr
from .enums.error2 import Error2OrStr
from .enums.status8 import Status8OrStr


class Upload(SdkBaseModel):
    """The video's upload information."""

    approach: Optional[ApproachOrStr] = UNSET
    """The approach for uploading the video.

    Option descriptions:
     * ``post`` - The video upload uses the POST approach.
     * ``pull`` - The video upload uses the pull approach.
     * ``tus`` - The video upload uses the tus approach."""

    error: Optional[Error2OrStr] = UNSET
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

    form: Optional[str] = UNSET
    """The HTML form for uploading a video through the POST approach."""

    gcs_uid: Optional[str] = UNSET
    """The ID of the Google Cloud Storage upload."""

    link: Optional[str] = UNSET
    """The link of the video to capture through the pull approach."""

    redirect_url: Optional[str] = UNSET
    """The redirect URL for the upload app."""

    size: Optional[float] = UNSET
    """The file size in bytes of the uploaded video."""

    status: Status8OrStr
    """The status code for the availability of the uploaded video.

    Option descriptions:
     * ``canceled`` - The upload was canceled.
     * ``complete`` - The upload is complete.
     * ``error`` - The upload ended with an error.
     * ``in_progress`` - The upload is underway."""

    upload_link: Optional[str] = UNSET
    """The link for sending video file data."""


class UploadDict(TypedDict):
    approach: NotRequired[ApproachOrStr]
    error: NotRequired[Error2OrStr]
    form: NotRequired[str]
    gcs_uid: NotRequired[str]
    link: NotRequired[str]
    redirect_url: NotRequired[str]
    size: NotRequired[float]
    status: Status8OrStr
    upload_link: NotRequired[str]
