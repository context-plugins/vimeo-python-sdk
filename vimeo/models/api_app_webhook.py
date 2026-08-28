from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.webhook_type import WebhookTypeOrStr


class ApiAppWebhook(SdkBaseModel):
    app_uri: float
    """The URI of the API app for which the webhook is created."""

    created_on: str
    """The time in ISO 8601 format when the webhook was created."""

    disabled_on: Optional[str] = UNSET
    """The time in ISO 8601 format when the webhook was most recently disabled. If this field isn't present in the
    response, the webhook isn't disabled."""

    enabled_on: Optional[str] = UNSET
    """The time in ISO 8601 format when the webhook was most recently enabled. If this field doesn't appear in the
    response, the webhook is disabled."""

    failure_rate_before_disabling: Optional[float] = UNSET
    """The failure error rate at the time that the webhook was most recently disabled. If this field doesn't appear in
    the response, the webhook wasn't disabled after being active."""

    is_enabled: bool
    """Whether the webhook is activated."""

    last_request_time_before_disabling: Optional[str] = UNSET
    """The time in ISO 8601 format when the last request to the webhook URL was made before the webhook was disabled. If
    this field doesn't appear in the response, the webhook wasn't disabled after being active."""

    modified_on: str
    """The time in ISO 8601 format when the webhook was most recently modified."""

    requests_executed_before_disabling: Optional[float] = UNSET
    """The number of requests that were executed before the webhook was most recently disabled. If this field doesn't
    appear in the response, the webhook wasn't disabled after being active."""

    requests_failed_before_disabling: Optional[float] = UNSET
    """The number of requests that failed before the webhook was most recently disabled. If this field doesn't appear in
    the response, the webhook wasn't disabled after being active."""

    secret: Optional[str] = UNSET
    """The secret key that is passed on webhook payloads. If this field isn't present in the response, no secret key is
    passed."""

    time_period_failure_rate: Optional[float] = UNSET
    """The time period in seconds over which requests were executed before the webhook was most recently disabled. If
    this field doesn't appear in the response, the webhook wasn't disabled after being active."""

    uri: str
    """The URI of the webhook."""

    webhook_type: WebhookTypeOrStr
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

    webhook_url: str
    """The URL to which data is sent when the webhook is triggered."""


class ApiAppWebhookDict(TypedDict):
    app_uri: float
    created_on: str
    disabled_on: NotRequired[str]
    enabled_on: NotRequired[str]
    failure_rate_before_disabling: NotRequired[float]
    is_enabled: bool
    last_request_time_before_disabling: NotRequired[str]
    modified_on: str
    requests_executed_before_disabling: NotRequired[float]
    requests_failed_before_disabling: NotRequired[float]
    secret: NotRequired[str]
    time_period_failure_rate: NotRequired[float]
    uri: str
    webhook_type: WebhookTypeOrStr
    webhook_url: str
