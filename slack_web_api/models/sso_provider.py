from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SsoProvider(SdkBaseModel):
    label: Optional[str] = UNSET
    name: Optional[str] = UNSET
    type_: Optional[str] = Field(default=UNSET, alias="type")


class SsoProviderDict(TypedDict):
    label: NotRequired[str]
    name: NotRequired[str]
    type_: NotRequired[str]
