from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class Defaultsuccesstemplate(SdkBaseModel):
    """This method either only returns a brief _OK_ response or a verbose schema is not available for this method."""

    ok: Literal["True"] = "True"


class DefaultsuccesstemplateDict(TypedDict):
    ok: NotRequired[Literal["True"]]
