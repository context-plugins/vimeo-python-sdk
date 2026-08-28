from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class ReactionsRemoveschema(SdkBaseModel):
    """Schema for successful response from reactions.remove method"""

    ok: Literal["True"] = "True"


class ReactionsRemoveschemaDict(TypedDict):
    ok: NotRequired[Literal["True"]]
