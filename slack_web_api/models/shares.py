from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Shares(SdkBaseModel):
    private: Optional[Any] = UNSET
    public: Optional[Any] = UNSET


class SharesDict(TypedDict):
    private: NotRequired[Any]
    public: NotRequired[Any]
