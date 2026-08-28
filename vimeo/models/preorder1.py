from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Preorder1(SdkBaseModel):
    active: Optional[bool] = UNSET
    """Whether to enable preorders on the On Demand page."""

    publish_time: Optional[str] = UNSET
    """The time in ISO 8601 format when the On Demand page will be published. This parameter is required when
    **preorder.active** is ``true``."""


class Preorder1Dict(TypedDict):
    active: NotRequired[bool]
    publish_time: NotRequired[str]
