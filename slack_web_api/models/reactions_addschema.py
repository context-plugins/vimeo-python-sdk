from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class ReactionsAddschema(SdkBaseModel):
    """Schema for successful response from reactions.add method"""

    ok: Literal["True"] = "True"


class ReactionsAddschemaDict(TypedDict):
    ok: NotRequired[Literal["True"]]
