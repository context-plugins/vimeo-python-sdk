from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .buy5 import Buy5, Buy5Dict
from .enums.type38 import Type38OrStr
from .rent5 import Rent5, Rent5Dict


class OndemandPagesVideosRequest(SdkBaseModel):
    buy: Optional[Buy5] = UNSET
    position: Optional[float] = UNSET
    """The position of the video in the On Demand collection."""

    release_year: Optional[float] = UNSET
    """The release year of the video."""

    rent: Optional[Rent5] = UNSET
    type_: Type38OrStr = Field(alias="type")
    """The type of the video.

    Option descriptions:
     * ``extra`` - The video type is extra footage.
     * ``main`` - The video type is the main video.
     * ``trailer`` - The video type is a trailer."""


class OndemandPagesVideosRequestDict(TypedDict):
    buy: NotRequired[Buy5 | Buy5Dict]
    position: NotRequired[float]
    release_year: NotRequired[float]
    rent: NotRequired[Rent5 | Rent5Dict]
    type_: Type38OrStr
