from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class LiveEventsActivateRequest(SdkBaseModel):
    cloud_composing_streaming: Optional[bool] = UNSET
    """Whether the stream activates from the cloud composer."""

    streaming_start_requested: Optional[bool] = UNSET
    """Whether the stream activates from the cloud composer."""


class LiveEventsActivateRequestDict(TypedDict):
    cloud_composing_streaming: NotRequired[bool]
    streaming_start_requested: NotRequired[bool]
