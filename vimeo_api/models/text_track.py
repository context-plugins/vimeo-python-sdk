from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .download_links import DownloadLinks, DownloadLinksDict
from .enums.provenance1 import Provenance1OrStr
from .enums.type24 import Type24OrStr
from .metadata27 import Metadata27, Metadata27Dict


class TextTrack(SdkBaseModel):
    active: bool
    """Whether the text track is active."""

    created_on: str
    """The time in ISO 8601 format when the text track was created."""

    display_language: str
    """The name of the language."""

    download_links: Optional[DownloadLinks] = UNSET
    """A map of read-only download URLs for the text track, keyed by file format."""

    download_links_expires_time: Optional[str] = UNSET
    """The time in ISO 8601 format when the URLs in ``download_links`` expire."""

    hls_link: str
    """The read-only URL of the text track file, intended for use with HLS playback."""

    hls_link_expires_time: str
    """The time in ISO 8601 format when the read-only HLS playback text track file expires."""

    id: float
    """The text track identifier."""

    language: str | None
    """The language code for the text track. To see a full list, request ``/languages?filter=texttrack``."""

    link: str
    """The read-only URL of the text track file. You can upload to this link when you create it for the first time."""

    link_expires_time: str
    """The time in ISO 8601 format when the text track link expires."""

    metadata: Optional[Metadata27] = UNSET
    modified_on: str
    """The time in ISO 8601 format when the text track was last modified."""

    name: str | None
    """The descriptive name of the text track."""

    provenance: Provenance1OrStr
    """The upload source of the text track.

    Option descriptions:
     * ``autogen_alternate_audio`` - The text track is automatically generated from alternate audio.
     * ``autogen_dubbed`` - The text track is automatically generated from AI dubbing.
     * ``autogen_live_audio`` - The text track is automatically generated from live audio.
     * ``autogen_source_audio`` - The text track is automatically generated from source audio.
     * ``autogen_translated`` - The text track is automatically generated from AI translation.
     * ``user_uploaded`` - The text track is uploaded by a user."""

    source_link: str
    """The read-only URL of the source text track file that was originally uploaded."""

    source_link_expires_time: str
    """The time in ISO 8601 format when the read-only source text track link expires."""

    type_: Type24OrStr | None = Field(alias="type")
    """The type of text track.

    Option descriptions:
     * ``captions`` - The text track is for captions.
     * ``subtitles`` - The text track is for subtitles."""

    uri: str
    """The relative URI of the text track."""

    version: float | None
    """The version of the text track. This data requires a bearer token with the ``private`` scope."""


class TextTrackDict(TypedDict):
    active: bool
    created_on: str
    display_language: str
    download_links: NotRequired[DownloadLinks | DownloadLinksDict]
    download_links_expires_time: NotRequired[str]
    hls_link: str
    hls_link_expires_time: str
    id: float
    language: str | None
    link: str
    link_expires_time: str
    metadata: NotRequired[Metadata27 | Metadata27Dict]
    modified_on: str
    name: str | None
    provenance: Provenance1OrStr
    source_link: str
    source_link_expires_time: str
    type_: Type24OrStr | None
    uri: str
    version: float | None
