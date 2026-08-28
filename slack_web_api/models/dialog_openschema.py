from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class DialogOpenschema(SdkBaseModel):
    """Schema for successful response from dialog.open method"""

    ok: Literal["True"] = "True"


class DialogOpenschemaDict(TypedDict):
    ok: NotRequired[Literal["True"]]
