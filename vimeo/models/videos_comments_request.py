from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class VideosCommentsRequest(SdkBaseModel):
    richtext: Optional[str] = UNSET
    """The rich comment in JSON stringified form. Either this field or the **text** field is required."""

    text: Optional[str] = UNSET
    """The comment as plain text. Either this field or the **richtext** field is required."""


class VideosCommentsRequestDict(TypedDict):
    richtext: NotRequired[str]
    text: NotRequired[str]
