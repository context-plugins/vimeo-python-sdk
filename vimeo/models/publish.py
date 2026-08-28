from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Publish(SdkBaseModel):
    active: Optional[bool] = UNSET
    """Whether to publish the On Demand page."""


class PublishDict(TypedDict):
    active: NotRequired[bool]
