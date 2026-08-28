from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class PinsAddschema(SdkBaseModel):
    """Schema for successful response from pins.add method"""

    ok: Literal["True"] = "True"


class PinsAddschemaDict(TypedDict):
    ok: NotRequired[Literal["True"]]
