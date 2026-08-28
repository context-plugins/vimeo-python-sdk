from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class ChatUnfurlsuccessschema(SdkBaseModel):
    """Schema for successful response from chat.unfurl method"""

    ok: Literal["True"] = "True"


class ChatUnfurlsuccessschemaDict(TypedDict):
    ok: NotRequired[Literal["True"]]
