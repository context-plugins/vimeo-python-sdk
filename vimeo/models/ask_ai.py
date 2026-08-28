from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class AskAi(SdkBaseModel):
    """Information about where and how to submit questions to the AI service for this video."""

    options: list[str]
    """An array of HTTP methods permitted on this URI."""

    uri: str
    """The API URI that resolves to the connection data."""


class AskAiDict(TypedDict):
    options: list[str]
    uri: str
