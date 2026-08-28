from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Preorder(SdkBaseModel):
    active: bool
    """Whether the On Demand page is available for preorder."""

    cancel_time: str
    """The time in ISO 8601 format when the preorder was cancelled."""

    publish_time: str
    """The time in ISO 8601 format when the preorder was released to the public."""

    time: str
    """The time in ISO 8601 format when the preorder started."""


class PreorderDict(TypedDict):
    active: bool
    cancel_time: str
    publish_time: str
    time: str
