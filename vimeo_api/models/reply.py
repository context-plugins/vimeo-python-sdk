from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel
from .metadata14 import Metadata14, Metadata14Dict
from .text_decoration import TextDecoration, TextDecorationDict


class Reply(SdkBaseModel):
    created_on: str
    """The time in ISO 8601 format when the reply was posted."""

    deleted_on: str | None
    """The time in ISO 8601 format when the reply was deleted."""

    last_edited_on: str | None
    """The time in ISO 8601 format when the reply was last edited."""

    link: str
    """The permalink to the reply."""

    metadata: Metadata14
    resource_key: str
    """The comment's resource key string."""

    richtext: str | None
    """The stringified Rich Text JSON."""

    text: str
    """The content of the reply."""

    text_decorations: list[TextDecoration]
    """An array of text decorations for the note."""

    type_: Literal["video"] = Field(default="video", alias="type")
    """The Vimeo content to which the reply relates.

    Option descriptions:
     * ``video`` - The comment is about a video."""

    uri: str
    """The unique identifier to access the reply resource."""


class ReplyDict(TypedDict):
    created_on: str
    deleted_on: str | None
    last_edited_on: str | None
    link: str
    metadata: Metadata14 | Metadata14Dict
    resource_key: str
    richtext: str | None
    text: str
    text_decorations: list[TextDecoration | TextDecorationDict]
    type_: NotRequired[Literal["video"]]
    uri: str
