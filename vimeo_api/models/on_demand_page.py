from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .colors2 import Colors2, Colors2Dict
from .enums.type9 import Type9OrStr
from .episodes import Episodes, EpisodesDict
from .metadata9 import Metadata9, Metadata9Dict
from .on_demand_genre import OnDemandGenre, OnDemandGenreDict
from .picture import Picture, PictureDict
from .preorder import Preorder, PreorderDict
from .published import Published, PublishedDict
from .subscription1 import Subscription1, Subscription1Dict
from .user import User, UserDict
from .video import Video, VideoDict


class OnDemandPage(SdkBaseModel):
    background: Picture | None
    """The background image for the On Demand page."""

    colors: Colors2
    """The first and second colors of the On Demand page."""

    content_rating: list[str]
    """An array of the On Demand page's content ratings."""

    created_time: Optional[str] = UNSET
    """The time in ISO 8601 format when the On Demand page was created."""

    description: str | None
    """The description of the On Demand page."""

    domain_link: str | None
    """The link to the On Demand page on its own domain."""

    episodes: Episodes
    """Information about the On Demand page's episodes, if the page is for a series."""

    film: Optional[Video] = UNSET
    """The On Demand page's film, if the page is for a film."""

    genres: list[OnDemandGenre]
    """An array of the genres assigned to the On Demand page."""

    link: str
    """The link to the On Demand page."""

    metadata: Metadata9
    """Metadata about the On Demand page."""

    modified_time: Optional[str] = UNSET
    """The time in ISO 8601 format when the On Demand page was last modified."""

    name: str
    """The descriptive title of the On Demand page."""

    pictures: Picture | None
    """The active poster for the On Demand page."""

    preorder: Preorder
    published: Published
    rating: float | None
    """The rating of the On Demand page."""

    resource_key: str
    """The On Demand resource key."""

    sku: OptionalNullable[str] = UNSET
    """The creator-designated SKU for the On Demand page."""

    subscription: Subscription1 | None
    """Information about subscribing to the On Demand page, if subscription is enabled."""

    theme: str
    """The graphical theme for the On Demand page."""

    thumbnail: Picture | None
    """The thumbnail image for the On Demand page."""

    trailer: Video | None
    """The trailer for the On Demand page."""

    type_: Type9OrStr = Field(alias="type")
    """The type of the On Demand page.

    Option descriptions:
     * ``film`` - The On Demand page is for a film.
     * ``series`` - The On Demand page is for a series."""

    uri: str
    """The relative URI of the On Demand page."""

    user: User | None
    """The user who created the On Demand page."""


class OnDemandPageDict(TypedDict):
    background: PictureDict | None
    colors: Colors2Dict
    content_rating: list[str]
    created_time: NotRequired[str]
    description: str | None
    domain_link: str | None
    episodes: EpisodesDict
    film: NotRequired[VideoDict]
    genres: list[OnDemandGenreDict]
    link: str
    metadata: Metadata9Dict
    modified_time: NotRequired[str]
    name: str
    pictures: PictureDict | None
    preorder: PreorderDict
    published: PublishedDict
    rating: float | None
    resource_key: str
    sku: NotRequired[str | None]
    subscription: Subscription1Dict | None
    theme: str
    thumbnail: PictureDict | None
    trailer: VideoDict | None
    type_: Type9OrStr
    uri: str
    user: UserDict | None
