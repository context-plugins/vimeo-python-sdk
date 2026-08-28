from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class WebhookType(str, Enum):
    """The type of event that triggers the webhook.

    Option descriptions:
     * ``automatic-thumbnail-available`` - The webhook is called when the automatically generated thumbnail is
            available.
     * ``live-event-archive-available`` - The webhook is called when an archive of the event is available.
     * ``live-event-clip-created`` - The webhook is called when a new video of the event is created.
     * ``live-event-deleted`` - The webhook is called when an event is deleted.
     * ``live-event-ended`` - The webhook is called when an event is ended.
     * ``live-event-started`` - The webhook is called when an event is started.
     * ``live-event-updated`` - The webhook is called when an event is updated.
     * ``transcript-status-complete`` - The webhook is called when a transcript status is either ``completed`` or
            ``failed``.
     * ``transcript-status-updated`` - The webhook is called when a transcript status is updated.
     * ``video-created`` - The webhook is called when a video is created.
     * ``video-deleted`` - The webhook is called when a video is deleted.
     * ``video-transcode-complete`` - The webhook is called when a video finishes transcoding.
     * ``video-transcode-fully-playable`` - The webhook is called when a video is playable in all resolutions, up to
            either the source quality or 4K, whichever is lower, at standard definition.
     * ``video-transcode-playable`` - The webhook is called when a video is playable.
     * ``video-updated`` - The webhook is called when a video is updated.
     * ``video-upload-failed`` - The webhook is called when a video upload fails."""

    AUTOMATIC_THUMBNAIL_AVAILABLE = "automatic-thumbnail-available"
    LIVE_EVENT_ARCHIVE_AVAILABLE = "live-event-archive-available"
    LIVE_EVENT_CLIP_CREATED = "live-event-clip-created"
    LIVE_EVENT_DELETED = "live-event-deleted"
    LIVE_EVENT_ENDED = "live-event-ended"
    LIVE_EVENT_STARTED = "live-event-started"
    LIVE_EVENT_UPDATED = "live-event-updated"
    TRANSCRIPT_STATUS_COMPLETE = "transcript-status-complete"
    TRANSCRIPT_STATUS_UPDATED = "transcript-status-updated"
    VIDEO_CREATED = "video-created"
    VIDEO_DELETED = "video-deleted"
    VIDEO_TRANSCODE_COMPLETE = "video-transcode-complete"
    VIDEO_TRANSCODE_FULLY_PLAYABLE = "video-transcode-fully-playable"
    VIDEO_TRANSCODE_PLAYABLE = "video-transcode-playable"
    VIDEO_UPDATED = "video-updated"
    VIDEO_UPLOAD_FAILED = "video-upload-failed"

    __str__ = str.__str__


WebhookTypeOrStr: TypeAlias = Annotated[WebhookType | str, open_enum_validator(WebhookType)]
