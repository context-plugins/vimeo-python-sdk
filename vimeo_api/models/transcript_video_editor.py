from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class TranscriptVideoEditor(SdkBaseModel):
    """Information about where and how to edit a video using the Transcription-based Video Editor editor."""

    options: list[str]
    """An array of HTTP methods permitted on this URI."""

    uri: str
    """The URI that resolves to the connection data."""


class TranscriptVideoEditorDict(TypedDict):
    options: list[str]
    uri: str
