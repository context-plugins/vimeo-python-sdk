from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.type25 import Type25OrStr


class VideosTexttracksRequest(SdkBaseModel):
    active: Optional[bool] = UNSET
    """Whether the current text track is the *active text track,* or the one that appears in the player. Only one text
    track per language and type can be active."""

    is_auto_generated: Optional[bool] = UNSET
    """Whether the text track was uploaded automatically by the Seshat audio annotation management platform."""

    is_edited: Optional[bool] = UNSET
    """Whether the text track was uploaded by the Seshat audio annotation management platform after the user edited
    their transcript."""

    language: str
    """The language of the text track. For a full list of supported languages, use the
    https://developer.vimeo.com/api/reference/videos#get_languages endpoint."""

    name: str
    """The name of the text track."""

    type_: Type25OrStr = Field(alias="type")
    """The type of text track.

    Option descriptions:
     * ``captions`` - The text track is the captions type.
     * ``chapters`` - The text track is the chapters type.
     * ``descriptions`` - The text track is the descriptions type.
     * ``metadata`` - The text track is the metadata type.
     * ``subtitles`` - The text track is the subtitles type."""


class VideosTexttracksRequestDict(TypedDict):
    active: NotRequired[bool]
    is_auto_generated: NotRequired[bool]
    is_edited: NotRequired[bool]
    language: str
    name: str
    type_: Type25OrStr
