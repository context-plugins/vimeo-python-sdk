from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ReviewPage(SdkBaseModel):
    active: Optional[bool] = UNSET
    """Whether to enable video review."""


class ReviewPageDict(TypedDict):
    active: NotRequired[bool]
