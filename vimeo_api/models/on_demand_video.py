from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .buy2 import Buy2, Buy2Dict
from .enums.type23 import Type23OrStr
from .interactions13 import Interactions13, Interactions13Dict
from .metadata21 import Metadata21, Metadata21Dict
from .picture import Picture, PictureDict
from .rent2 import Rent2, Rent2Dict
from .user import User, UserDict


class OnDemandVideo(SdkBaseModel):
    buy: Buy2 | None
    """Information about purchasing the video."""

    description: Optional[str] = UNSET
    """The description of the video."""

    duration: Optional[str] = UNSET
    """The duration of the video."""

    episode: Optional[float] = UNSET
    """The episode number of the video."""

    interactions: Interactions13
    """An object containing information about how the authenticated user can interact with the video's On Demand
    page."""

    link: str
    """The link to the video on Vimeo."""

    metadata: Metadata21
    """Metadata information about the video."""

    name: Optional[str] = UNSET
    """The title of the video."""

    options: Optional[list[str]] = UNSET
    """An array of HTTP methods permitted on this URI."""

    pictures: Optional[Picture] = UNSET
    """The active picture of the video."""

    play_progress: float
    """The authenticated user's most recent play position in the video, in seconds."""

    position: Optional[float] = UNSET
    """The position of the video relative to the other videos on the On Demand page."""

    release_date: Optional[str] = UNSET
    """The time in ISO 8601 format when the video was created or published."""

    release_year: float | None
    """The year that the video was released."""

    rent: Rent2 | None
    """Information about renting the video."""

    type_: Type23OrStr = Field(alias="type")
    """The type of video.

    Option descriptions:
     * ``extra`` - The video is an extra feature.
     * ``main`` - The video is a main feature.
     * ``trailer`` - The video is a trailer."""

    uri: str
    """The video container's relative URI."""

    user: Optional[User] = UNSET
    """The owner of the video."""


class OnDemandVideoDict(TypedDict):
    buy: Buy2Dict | None
    description: NotRequired[str]
    duration: NotRequired[str]
    episode: NotRequired[float]
    interactions: Interactions13Dict
    link: str
    metadata: Metadata21Dict
    name: NotRequired[str]
    options: NotRequired[list[str]]
    pictures: NotRequired[PictureDict]
    play_progress: float
    position: NotRequired[float]
    release_date: NotRequired[str]
    release_year: float | None
    rent: Rent2Dict | None
    type_: Type23OrStr
    uri: str
    user: NotRequired[UserDict]
