from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.webhook_type1 import WebhookType1OrStr


class AppsWebhooksRequest1(SdkBaseModel):
    is_enabled: Optional[bool] = UNSET
    """Whether the webhook is activated."""

    secret: OptionalNullable[str] = UNSET
    """The secret key that is passed on webhook payloads. The null value means that no secret key is passed."""

    webhook_type: Optional[WebhookType1OrStr] = UNSET
    """The type of event that triggers the webhook.

    Option descriptions:
     * ``automatic-thumbnail-available`` - The webhook is called when the automatically generated thumbnail is
            available.
     * ``content-scan-completed`` - The webhook is called when content moderation scan results are available.
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

    webhook_url: Optional[str] = UNSET
    """The URL to which data is sent."""


class AppsWebhooksRequest1Dict(TypedDict):
    is_enabled: NotRequired[bool]
    secret: NotRequired[str | None]
    webhook_type: NotRequired[WebhookType1OrStr]
    webhook_url: NotRequired[str]
