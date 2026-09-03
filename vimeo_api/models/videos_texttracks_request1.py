from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.type25 import Type25OrStr


class VideosTexttracksRequest1(SdkBaseModel):
    active: Optional[bool] = UNSET
    """Whether the current text track is the *active text track,* or the one that appears in the player. Only one text
    track per language and per type can be active."""

    language: Optional[str] = UNSET
    """The language of the text track. For a full list of supported languages, use the
    https://developer.vimeo.com/api/reference/videos#get_languages endpoint."""

    name: Optional[str] = UNSET
    """The name of the text track."""

    type_: Optional[Type25OrStr] = Field(default=UNSET, alias="type")
    """The type of text track.

    Option descriptions:
     * ``captions`` - The text track is the captions type.
     * ``chapters`` - The text track is the chapters type.
     * ``descriptions`` - The text track is the descriptions type.
     * ``metadata`` - The text track is the metadata type.
     * ``subtitles`` - The text track is the subtitles type."""


class VideosTexttracksRequest1Dict(TypedDict):
    active: NotRequired[bool]
    language: NotRequired[str]
    name: NotRequired[str]
    type_: NotRequired[Type25OrStr]
