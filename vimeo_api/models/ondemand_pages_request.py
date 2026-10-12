from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .preorder1 import Preorder1, Preorder1Dict
from .publish import Publish, PublishDict


class OndemandPagesRequest(SdkBaseModel):
    link: Optional[str] = UNSET
    """The custom string to use in the Vimeo URL of the On Demand page."""

    preorder: Optional[Preorder1] = UNSET
    publish: Optional[Publish] = UNSET
    publish_when_ready: Optional[bool] = UNSET
    """Whether to publish the On Demand page automatically after all videos have finished transcoding."""


class OndemandPagesRequestDict(TypedDict):
    link: NotRequired[str]
    preorder: NotRequired[Preorder1Dict]
    publish: NotRequired[PublishDict]
    publish_when_ready: NotRequired[bool]
