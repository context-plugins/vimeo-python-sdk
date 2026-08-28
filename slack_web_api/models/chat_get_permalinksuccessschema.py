from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class ChatGetPermalinksuccessschema(SdkBaseModel):
    """Schema for successful response chat.getPermalink"""

    channel: str
    ok: Literal["True"] = "True"
    permalink: str


class ChatGetPermalinksuccessschemaDict(TypedDict):
    channel: str
    ok: NotRequired[Literal["True"]]
    permalink: str
