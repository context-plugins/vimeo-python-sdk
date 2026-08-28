from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class Defaulterrortemplate1Error(SdkBaseModel):
    """This method either only returns a brief _not OK_ response or a verbose schema is not available for this
    method."""

    ok: Literal["False"] = "False"


class Defaulterrortemplate1ErrorDict(TypedDict):
    ok: NotRequired[Literal["False"]]
