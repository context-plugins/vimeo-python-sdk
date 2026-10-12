from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.type15 import Type15OrStr
from .metadata13 import Metadata13, Metadata13Dict
from .metdata import Metdata, MetdataDict
from .reply import Reply, ReplyDict
from .text_decoration import TextDecoration, TextDecorationDict
from .user import User, UserDict


class Comment(SdkBaseModel):
    created_on: str
    """The time in ISO 8601 format when the comment was posted."""

    deleted_on: str | None
    """The time in ISO 8601 format when the comment was deleted."""

    last_edited_on: str | None
    """The time in ISO 8601 format when the comment was last edited."""

    link: str
    """The permalink to the comment."""

    metadata: Metadata13
    metdata: Metdata
    replies: list[Reply]
    """The list of replies to the comment."""

    resource_key: str
    """The comment's resource key string."""

    richtext: str | None
    """The stringified Rich Text JSON."""

    text: str
    """The content of the comment."""

    text_decorations: list[TextDecoration]
    """An array of text decorations for the note."""

    type_: Type15OrStr = Field(alias="type")
    """The Vimeo content to which the comment relates.

    Option descriptions:
     * ``video`` - The comment is about a video."""

    uri: str
    """The unique identifier to access the comment resource."""

    user: User | None
    """The user who posted the comment. _This field is deprecated. Use the **metadata.connections.user** field
    instead._"""


class CommentDict(TypedDict):
    created_on: str
    deleted_on: str | None
    last_edited_on: str | None
    link: str
    metadata: Metadata13Dict
    metdata: MetdataDict
    replies: list[ReplyDict]
    resource_key: str
    richtext: str | None
    text: str
    text_decorations: list[TextDecorationDict]
    type_: Type15OrStr
    uri: str
    user: UserDict | None
