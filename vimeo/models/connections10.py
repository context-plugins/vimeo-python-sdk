from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .comments3 import Comments3, Comments3Dict
from .genres import Genres, GenresDict
from .likes2 import Likes2, Likes2Dict
from .pictures2 import Pictures2, Pictures2Dict
from .seasons import Seasons, SeasonsDict
from .videos8 import Videos8, Videos8Dict


class Connections10(SdkBaseModel):
    comments: Comments3
    """Information about the comments associated with the On Demand page."""

    genres: Genres
    """Information about the genres associated with the On Demand page."""

    likes: Likes2
    """Information about the likes associated with the On Demand page."""

    pictures: Pictures2
    """Information about the pictures associated with the On Demand page."""

    seasons: Seasons
    """Information about the seasons associated with the On Demand page."""

    videos: Videos8
    """Information about the videos associated with the On Demand page."""


class Connections10Dict(TypedDict):
    comments: Comments3 | Comments3Dict
    genres: Genres | GenresDict
    likes: Likes2 | Likes2Dict
    pictures: Pictures2 | Pictures2Dict
    seasons: Seasons | SeasonsDict
    videos: Videos8 | Videos8Dict
